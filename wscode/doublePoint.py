class DoublePoint(object):
    def __init__(self) -> None:
        return
    
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    # 判断是否有环
    def cycle_detect(self, head):
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
    
    # 判断是否有环，如果有环则返回环的起点
    def cycle_head(self, head):
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

    # 无环单链表的中点
    def uncycle_middle(self, head):
        result = None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        result = slow
        return result
    
    # 无环单链表的倒数第 k 个元素
    def uncycle_last(self, head, k):
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

    '''
    最小覆盖子串：
    
    给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
    '''
    def leetcode_76(self, s, t):
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
    
    '''
    字符串的排列：
    
    给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

    换句话说，s1 的排列之一是 s2 的 子串 。
    '''
    def leetcode_576(self, s1: str, s2: str) -> bool:
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
