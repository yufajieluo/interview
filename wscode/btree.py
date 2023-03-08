#!/usr/bin/python
# -*- coding:utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# @File: btree.py
# @Time: 2023/03/07 22:12:06
# @Author: WShuai.
# @License : (C)Copyright 2023 WShuai.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Btree(object):
    def __init__(self) -> None:
        return

    def dlr(self, root: Optional[TreeNode]):     
        '''
        前序遍历
        '''
        result = []
        self.dlr_real(root, result)
        return result

    def dlr_real(self, root: Optional[TreeNode], result: List[int]):
        '''
        前序遍历 - 递归
        '''
        if not root:
            return
        result.append(root.val)
        self.dlr_real(root.left, result)
        self.dlr_real(root.right, result)
        return result

    def ldr(self, root: Optional[TreeNode]):
        '''
        中序遍历
        '''
        result = []
        self.ldr_real(root, result)
        return result

    def ldr_real(self, root: Optional[TreeNode], result: List[int]):
        '''
        中序遍历 - 递归
        '''
        if not root:
            return
        self.ldr_real(root.left, result)
        result.append(root.val)
        self.ldr_real(root.right, result)
        return result

    def lrd(self, root: Optional[TreeNode]):
        '''
        后序遍历
        '''
        result = []
        self.lrd_real(root, result)
        return result

    def lrd_real(self, root: Optional[TreeNode], result: List[int]):
        '''
        后序遍历 - 递归
        '''
        if not root:
            return
        self.lrd_real(root.left, result)
        self.lrd_real(root.right, result)
        result.append(root.val)
        return result

    def dfs(self, root: Optional[TreeNode]):
        result = []



        return result

    def bfs(self, root: Optional[TreeNode]):
        '''
        广度优先遍历 - 迭代
        '''
        result = []

        queue = [root]
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


    def leetcode_104(self, root: TreeNode) -> int:
        '''
        二叉树的最大深度
        '''
        result = 0

        if root:
            queue = [root]
            while queue:
                result += 1
                current_size = len(queue)
                for _ in range(current_size):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        
        return result


    def leetcode_111(self, root: Optional[TreeNode]) -> int:
        '''
        二叉树的最小深度
        '''
        result = 0

        if root:
            queue = [root]
            while queue:
                result += 1
                current_size = len(queue)
                leaf = False
                for _ in range(current_size):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    if not node.left and not node.right:
                        leaf = True
                        break
                if leaf:
                    break
                
        return result

if __name__ == '__main__':
    root = TreeNode(-10, None, None)
    node_9 = TreeNode(9, None, None)
    node_20 = TreeNode(20, None, None)
    node_15 = TreeNode(15, None, None)
    node_7   = TreeNode(7, None, None)
    root.left = node_9
    root.right = node_20
    node_20.left = node_15
    node_20.right = node_7

    btree = Btree()
    result = btree.dlr(root)
    print(result)
    result = btree.ldr(root)
    print(result)
    result = btree.lrd(root)
    print(result)
    result = btree.bfs_queue(root)
    print(result)

