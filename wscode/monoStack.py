#!/usr/bin/python
# -*- coding:utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# @File: monoStack.py
# @Time: 2023/03/05 23:38:59
# @Author: WShuai.
# @License : (C)Copyright 2023 WShuai.

from typing import List

class Stack(object):
    def __init__(self):
        self.stack = []
        return

    def is_empty(self):
        result = True if not self.stack else False
        return result

    def top(self):
        result = None
        if not self.is_empty():
            result = self.stack[-1]
        else:
            result = -1
        return result

    def push(self, value):
        self.stack.append(value)
        return
    
    def pop(self):
        result = None
        if not self.is_empty():
            result = self.stack.pop()
        else:
            result = -1
        return result


class MonoStack(object):
    def __init__(self) -> None:
        return
    
    def monotonic(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)

        stack = Stack()

        index = len(nums) - 1
        while index >= 0:
            while not stack.is_empty() and nums[index] >= stack.top():
                stack.pop()
            result[index] = stack.top()
            stack.push(nums[index])
            index -= 1
        return result

    def leetcode_503(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        result = [-1] * len_nums

        stack = Stack()

        index = len_nums * 2 - 1
        while index >= 0:
            while not stack.is_empty() and nums[index % len_nums] >= stack.top():
                stack.pop()
            result[index % len_nums] = stack.top()
            stack.push(nums[index % len_nums])
            index -= 1
        
        return result
    
    def leetcode_739(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = Stack()

        index = len(temperatures) - 1
        while index >= 0:
            while not stack.is_empty() and temperatures[index] >= temperatures[stack.top()]:
                stack.pop()
            result[index] = (stack.top() - index) if not stack.is_empty() else 0
            stack.push(index)
            index -= 1

        return result
    
if __name__ == '__main__':
    mono_stack = MonoStack()
    nums = [1,2,1]
    result = mono_stack.leetcode_503(nums)
    print('result is {}'.format(result))