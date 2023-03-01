
from typing import List

class Search(object):
    def __init__(self) -> None:
        return
    
    
    def leetcode_704(self, nums: List[int], target: int) -> int:
        '''
        二分查找
        '''
        result = -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                result = middle
                break

        return result
    
    
    def binary_bound_left(self, nums, target):
        '''
        二分查找左边界
        '''

        result = -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        
        if left >= len(nums) or target != nums[left]:
            result = -1
        else:
            result = left

        return result
    
   
    def binary_bound_right(self, nums, target):
        '''
        二分查找右边界
        '''

        result = -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                left = middle + 1
        
        if right < 0 or target != nums[right]:
            result = -1
        else:
            result = right

        return result
