class Search(object):
    def __init__(self) -> None:
        return
    
    # 二分查找普通
    def binary(self, nums, target):
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
    
    # 二分查找左边界
    def binary_bound_left(self, nums, target):
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
    
    # 二分查找右边界
    def binary_bound_right(self, nums, target):
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
