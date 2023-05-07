# Docker



## 优点

-   资源利用率更高
-   启动时间更快
-   运行环境一致
-   部署交付更便捷

## 1. 镜像

![1683469074982](C:\Users\wcy\AppData\Roaming\Typora\typora-user-images\1683469074982.png)

-   Union FIle System 联合文件系统，把不用的每一层，整合为一个文件系统，为用户隐藏了多层的视角
-   Bootfs 主要包含 bootloader（引导加载kernel）、kernel，Linux启动时会加载 Bootfs
-   Rootfs 不同操作系统的发行版，比如 Ubuntu、CentOS等，主要包含 /dev、/proc、/bin、/etc 等标准目录和文件
-   Image的本质是基于UnionFS管理的分层文件系统
-   由于只有 Rootfs及以上的层，使用宿主机的Bootfs，因此Image要比完整的系统要小
-   分层原因
    -   资源共享，上层镜像可以复用下层镜像
    -   方便镜像的分发和存储
-   启动一个容器时，会在 Image 的最顶层，添加一个writable的层，这一层通常被称为容器层，而此时下面的所有都被称为镜像层
    -   所有对容器的修改动作，都只会发生在这个容器层
    -   添加文件：新文件被添加到容器层
    -   读取文件：读取某个文件时，会从上到下依次在各镜像层中查找此文件，找到后复制到容器层，然后打开并读取到内存
    -   修改文件：修改某个文件时，会从上到下依次在各镜像层中查找此文件，找到后复制到容器层，然后修改
    -   删除文件：修改某个文件时，会从上到下依次在各镜像层中查找此文件，找到后，在容器层记录删除操作

## 2. 容器

-   容器的进程必须处于前台运行状态，否则容器会直接退出

## 3. 仓库

## 4. Dockerfile



```dockerfile
FROM
MAINTAINER
RUN
ADD
COPY
USER
WORKDIR
ARG
ENV
VOLUME
EXPOSE
CMD
```

-   entrypoint
    -   指定容器启动程序及参数
    -   当有entrypoint时，docker run 中的 CMD 内容会作为entrypoint的参数

-   ENV
    -   无论是Image构建时，还是容器运行时，定义的变量都可以使用
-   ARG
    -   Image构建时可以使用，容器运行时已被销毁，不可使用





## 命令

```shell
# Image
docker search ${image_name}:${image_tag}

docker pull ${image_name}:${image_tag}

docker images
	-q
	--format

docker info
docker images inspect ${image_id}

docker rmi ${image_name}:${image_tag}
docker rmi ${image_id}

docker ps
	-a

docker image save ${image_name}:${image_tag} > ${tar_path_file}
docker image load -i ${tar_path_file}


# Container

docker run 
	-i
	-t
	-d
	-p
	-v
	--rm
	--name

docker exec -it ${container_id} bash

docker port ${container_id}

docker inspect ${container_id}

docker stop ${container_id}

docker logs -f ${container_id}

docker rm ${container_id}

docker commit ${container_id} ${image_name}

# Dockerfile

docker build -t ${tag} .

```

