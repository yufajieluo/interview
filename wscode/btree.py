#!/usr/bin/python
# -*- coding:utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# @File: btree.py
# @Time: 2023/03/07 22:12:06
# @Author: WShuai.
# @License : (C)Copyright 2023 WShuai.

import copy
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
    
    def dlr_iteration(self, root: Optional[TreeNode]):
        '''
        前序遍历 - 迭代
        '''
        result = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                    stack.append(node)
                    stack.append(None)
                else:
                    result.append(stack.pop().val)
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

    def ldr_iteration(self, root: Optional[TreeNode]):
        '''
        中序遍历 - 迭代
        '''
        result = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    if node.right:
                        stack.append(node.right)
                    stack.append(node)
                    stack.append(None)
                    if node.left:
                        stack.append(node.left)
                else:
                    result.append(stack.pop().val)
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

    def ldr_iteration(self, root: Optional[TreeNode]):
        '''
        后序遍历 - 迭代
        '''
        result = []
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    stack.append(node)
                    stack.append(None)
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                else:
                    result.append(stack.pop().val)
        return result

    def bfs(self, root: Optional[TreeNode]):
        '''
        广度优先遍历 - 迭代
        '''
        result = []

        if root:
            queue = [root]
            while queue:
                node = queue.pop(0)
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def bfs_default_val(self, root: Optional[TreeNode]):
        '''
        广度优先遍历 - 迭代 - 带空值
        '''
        result = []
        default_value = 0

        if root:
            queue = [root]
            while queue:
                node = queue.pop(0)
                if not node:
                    result.append(default_value)
                else:
                    result.append(node.val)
                    queue.append(node.left)
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


    def plus(self, source, index):
        val = (int(source[index]) + 1) % 10
        return '{}{}{}'.format(source[:index], val, source[index+1:])

    def minus(self, source, index):
        val = (int(source[index]) - 1) % 10
        return '{}{}{}'.format(source[:index], val, source[index+1:])

    def leetcode_752(self, deadends: List[str], target: str) -> int:
        result = -1
        search = None
        visited = set()

        root = '0000'
        queue = [root]
        visited.add(root)

        depth = 0
        while queue:
            current_size = len(queue)
            for _ in range(current_size):
                node = queue.pop(0)
                if node in deadends:
                    continue
                if node == target:
                    search = True
                    break
                for index in range(4):
                    next_node_plus = self.plus(node, index)
                    if next_node_plus not in visited:
                        queue.append(next_node_plus)
                        visited.add(next_node_plus)
                    
                    next_node_minus = self.minus(node, index)
                    if next_node_minus not in visited:
                        queue.append(next_node_minus)
                        visited.add(next_node_minus)
            
            if search:
                break
            else:
                depth += 1
        
        result = depth if search else -1
        return result

    def search_space(self, source, target):
        result = []
        for index_r, row in enumerate(source):
            for index_c, col in enumerate(row):
                if col == 0:
                    result = [index_r, index_c]
                    break
        return result

    def next_value(self, source, coord):
        result = []
        if coord[0] > 0:
            next_up = copy.deepcopy(source)
            next_up[coord[0] - 1][coord[1]], next_up[coord[0]][coord[1]] = next_up[coord[0]][coord[1]], next_up[coord[0] - 1][coord[1]]
            result.append(next_up)
        if coord[0] < len(source) - 1:
            next_down = copy.deepcopy(source)
            next_down[coord[0] + 1][coord[1]], next_down[coord[0]][coord[1]] = next_down[coord[0]][coord[1]], next_down[coord[0] + 1][coord[1]]
            result.append(next_down)
        if coord[1] > 0:
            next_left = copy.deepcopy(source)
            next_left[coord[0]][coord[1] - 1], next_left[coord[0]][coord[1]] = next_left[coord[0]][coord[1]], next_left[coord[0]][coord[1] - 1]
            result.append(next_left)
        if coord[1] < len(source[0]) - 1:
            next_right = copy.deepcopy(source)
            next_right[coord[0]][coord[1] + 1], next_right[coord[0]][coord[1]] = next_right[coord[0]][coord[1]], next_right[coord[0]][coord[1] + 1]
            result.append(next_right)
        return result

    def leetcode_773(self, board: List[List[int]], target: List[List[int]]) -> int:
        result = -1
        depth = 0
        search = False

        queue = [board]
        visited = set()
        visited.add(str(board))
        
        while queue:
            current_size = len(queue)
            for _ in range(current_size):
                node = queue.pop(0)
                if node == target:
                    search = True
                    break
                coord = self.search_space(node, 0)
                nodes = self.next_value(node, coord)
                for next in nodes:
                    if str(next) not in visited:
                        queue.append(next)
                        visited.add(str(next))
            
            if search:
                break
            else:
                depth += 1

        result = depth if search else -1
        return result

import time
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
    '''
    result = btree.dlr(root)
    print(result)
    result = btree.ldr(root)
    print(result)
    result = btree.lrd(root)
    print(result)
    result = btree.bfs_queue(root)
    print(result)
    
    print(btree.dlr_iteration(root))
   
    print(btree.openLock(["0201","0101","0102","1212","2002"], '0202'))
    '''
    

    source = [[1,2,3],[5,4,0]]
    print(btree.slidingPuzzle(source, [[1,2,3],[4,5,0]]))