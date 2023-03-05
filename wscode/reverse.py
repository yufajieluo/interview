#!/usr/bin/python
# -*- coding:utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# @File: reverse.py
# @Time: 2023/03/02 22:27:17
# @Author: WShuai.
# @License : (C)Copyright 2023 WShuai.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        return
    
    def print(self):
        p = self
        while p:
            print(p.val)
            p = p.next
        return

class Reverse(object):
    def __init__(self) -> None:
        return
    
    def leetcode_206(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        反转链表 - 头插法
        '''

        result = None
        
        p_newh = ListNode(None, None)
        p_temp = ListNode(None, None)

        while head:
            p_temp = head
            head = head.next

            p_temp.next = p_newh.next
            p_newh.next = p_temp

        result = p_newh.next
        return result
    
    def leetcode_206_iteration(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        反转链表 - 迭代
        '''

        result = None

        p_cursor = head
        p_current_head = None
        p_last_head = None

        while p_cursor:
            p_current_head = p_cursor.next
            p_cursor.next = p_last_head
            p_last_head = p_cursor
            p_cursor = p_current_head

        result = p_last_head
        return result

    def leetcode_206_recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        反转链表 - 递归
        '''

        result = None

        if not head or not head.next:
            return head
        else:
            p_tail = self.leetcode_206_recursion(head.next)
            head.next.next = head
            head.next = None

        result = p_tail
        return result
    
    def leetcode_92(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
        '''
        
        result = None

        # 增加头指针
        p_hair = ListNode(None, head)

        # 找到起始位置
        p_middle_head = p_hair
        p_middle_tail = None
        for i in range(left):
            p_middle_tail = p_middle_head
            p_middle_head = p_middle_head.next
            
        # 反转到终止位置
        p_cursor = p_middle_head
        p_current_head = None
        p_last_head = None
        for i in range(right - left + 1):
            p_current_head = p_cursor.next
            p_cursor.next = p_last_head
            p_last_head = p_cursor
            p_cursor = p_current_head
            
        # 组装
        p_middle_tail.next = p_last_head
        p_middle_head.next = p_cursor

        result = p_hair.next
        return result
    
    def leetcode_25(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        K 个一组翻转链表

        给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

        k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

        你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
        '''

        result = head

        count = 0
        p_cursor = head
        while p_cursor:
            p_cursor = p_cursor.next
            if (count + 1) % k == 0:
                result = self.leetcode_92(result, count - k + 2, count + 1)          
            count += 1
            
        return result

    def lt(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = self.leetcode_92(head, 1, k)
        return result