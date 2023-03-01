import collections
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        return

class DoublePoint(object):
    def __init__(self) -> None:
        return
    

    def leetcode_141(self, head: Optional[ListNode]) -> bool:
        '''
        单链表是否有环
        '''
        result = False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                result = True
                break
        return result
    
    
    def leetcode_142(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        单链表是否有环，有环则返回环的起点
        '''
        result = False
        is_cycle = False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                is_cycle = True
                break
        
        if is_cycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            result = slow # or fast
        
        return result

    
    def leetcode_876(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        无环单链表的中点

        给你单链表的头结点 head ，请你找出并返回链表的中间结点。

        如果有两个中间结点，则返回第二个中间结点。
        '''

        result = None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        result = slow
        return result
    

    def leetcode_o22(self, head: ListNode, k: int) -> ListNode:
        '''
        无环单链表的倒数第 k 个元素

        输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

        例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
        '''
        result = None
        slow = head
        fast = head
        while k > 1:
            fast = fast.next
            k -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        result = slow
        return result

    # 翻转数组
    def reverse_array(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    
    def leetcode_76(self, s: str, t: str) -> str:
        '''
        最小覆盖子串：
        
        给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
        '''

        result = ''

        need = collections.defaultdict(int)
        wind = collections.defaultdict(int)
        for char in t:
            need[char] += 1

        left = 0
        right = 0
        valid = 0
        start, last_len = 0, len(s) + 1
        while right < len(s):
            # 右移窗口
            next_char = s[right]
            right += 1
            
            # 窗口内数据是否需要更新
            if next_char in need:
                wind[next_char] += 1
                if wind[next_char] == need[next_char]:
                    valid += 1
            
            print('wind [{}, {}]'.format(left, right))

            # 窗口是否需要左侧收缩
            while valid == len(need):
                if right - left < last_len:
                    start = left
                    last_len = right - left
                # 左移窗口
                remove_char = s[left]
                left += 1
                # 窗口内数据是否需要更新
                if remove_char in need:
                    if wind[remove_char] == need[remove_char]:
                        valid -= 1
                    wind[remove_char] -= 1
            
        result = s[start: start + last_len] if last_len < len(s) + 1 else ''
        return result
    
    
    def leetcode_576(self, s1: str, s2: str) -> bool:
        '''
        字符串的排列：
        
        给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

        换句话说，s1 的排列之一是 s2 的 子串 。
        '''

        result = False

        need = collections.defaultdict(int)
        wind = collections.defaultdict(int)
        for char in s1:
            need[char] += 1
        
        left, right = 0, 0
        valid = 0

        while right < len(s2):
            # 右扩窗口
            next_char = s2[right]
            right += 1

            # 窗口内数据是否需要更新
            if next_char in need:
                wind[next_char] += 1
                if wind[next_char] == need[next_char]:
                    valid += 1
            
            #print('wind is {}, left is {}, right is {}, valid is {}'.format(wind, left, right, valid))

            # 窗口是否需要左侧收缩
            while right - left >= len(s1):
                if valid == len(need):
                    result = True
                    return result
                else:
                    remove_char = s2[left]
                    left += 1
                    # 窗口内数据是否需要更新
                    if remove_char in need:
                        if wind[remove_char] == need[remove_char]:
                            valid -= 1
                        wind[remove_char] -= 1
        
        return result
    
    
    def leetcode_438(self, s: str, p: str) -> List[int]:
        '''
        找到字符串中所有字母异位词
        
        给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

        异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
        '''

        result = []

        need = collections.defaultdict(int)
        wind = collections.defaultdict(int)
        for char in p:
            need[char] += 1
        
        left, right = 0, 0
        valid = 0

        while right < len(s):
            # 右扩窗口
            next_char = s[right]
            right += 1

            # 窗口内数据是否需要更新
            if next_char in need:
                wind[next_char] += 1
                if wind[next_char] == need[next_char]:
                    valid += 1
            
            # 窗口是否需要左侧收缩
            while right - left >= len(p):
                if valid == len(need):
                    result.append(left)
                
                remove_char = s[left]
                left += 1

                # 窗口内数据是否需要更新
                if remove_char in need:
                    if wind[remove_char] == need[remove_char]:
                        valid -= 1
                    wind[remove_char] -= 1

        return result
    
    
    
    def leetcode_3(self, s: str) -> int:
        '''
        无重复字符的最长子串
        
        给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
        '''
        result = 0

        wind = collections.defaultdict(int)

        left, right = 0, 0
        while right < len(s):
            # 右扩窗口
            next_char = s[right]
            right += 1

            # 窗口内数据是否需要更新
            wind[next_char] += 1

            # 窗口是否需要左侧收缩
            while wind[next_char] > 1:
                remove_char = s[left]
                left += 1

                # 窗口内数据是否需要更新
                wind[remove_char] -= 1    
            
            result = max(result, right - left)
        
        return result
    
