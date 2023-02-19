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
