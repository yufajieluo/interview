import collections
from typing import List

class NSum(object):
    def __init__(self) -> None:
        return
    
    def leetcode_1(self, nums: List[int], target: int) -> List[int]:
        '''
        两数之和

        给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

        你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

        你可以按任意顺序返回答案
        '''
        result = []

        need = collections.defaultdict(int)

        for index, item in enumerate(nums):
            if target - item in need:
                result = [need[target - item], index]
                break
            else:
                need[item] = index

        return result

    
    def leetcode_1_2p(self, nums: List[int], target: int) -> List[int]:
        '''
        两数之和 - 双指针解法
        '''
        result = []

        nums.sort()
        left, right = 0, len(nums) - 1
       
        while left < right:
            left_current = nums[left]
            right_current = nums[right]
            sum_current = left_current + right_current
            if sum_current < target:
                while left < right and nums[left] == left_current:
                    left += 1
            elif sum_current > target:
                while left < right and nums[right] == right_current:
                    right -= 1
            else:
                result.append([left_current, right_current])
                while left < right and nums[left] == left_current:
                    left += 1
                while left < right and nums[right] == right_current:
                    right -= 1

        return result
    

    def leetcode_15(self, nums: List[int], target: int) -> List[int]:
        '''
        三数之和
        '''
        result = []

        nums.sort()

        last_item = None
        for index, item in enumerate(nums):
            if item != last_item:
                sums = self.twoSum(nums[index + 1 : ], target - item)
                for sum in sums:
                    sum.append(item)
                    result.append(sum)
                last_item = item

        return result
    

    def n_sum(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        '''
        N 数之和 - 递归
        '''
        nums.sort()
        result = self.sum(nums, target, n)
        return result
    
    def sum(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        result = []
        nums_len = len(nums)

        if n < 2 or nums_len < n:
            return result
        
        if n == 2:
            left_p, right_p = 0, nums_len - 1
            while left_p < right_p:
                left_value = nums[left_p]
                right_value = nums[right_p]
                current_sum = left_value + right_value
                if current_sum < target:
                    while left_p < right_p and nums[left_p] == left_value:
                        left_p += 1
                elif current_sum > target:
                    while left_p < right_p and nums[right_p] == right_value:
                        right_p -= 1
                else:
                    result.append([nums[left_p], nums[right_p]])
                    while left_p < right_p and nums[left_p] == left_value:
                        left_p += 1
                    while left_p < right_p and nums[right_p] == right_value:
                        right_p -= 1
        else:
            last_item = None
            for index, item in enumerate(nums):
                if item != last_item:
                    current_result = self.sum(nums[index + 1 : ], target - item, n - 1)
                    for cr in current_result:
                        cr.append(item)
                        result.append(cr)
                    last_item = item

        return result