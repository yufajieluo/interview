#!/usr/bin/python
# -*- coding:utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# @File: preSum.py
# @Time: 2023/03/05 12:03:27
# @Author: WShuai.
# @License : (C)Copyright 2023 WShuai.

import collections
from typing import List

class PreSum(object):
    def __init__(self) -> None:
        return
    
    def leetcode_560(self, nums: List[int], k: int) -> int:
        result = 0

        pre_sum_hash = collections.defaultdict(int)
        pre_sum_hash[0] = 1
        
        current_sum = 0
        for num in nums:
            current_sum += num
            
            if current_sum - k in pre_sum_hash:
                result += pre_sum_hash[current_sum - k]
            
            pre_sum_hash[current_sum] += 1
        
        return result

if __name__ == '__main__':
    pre_sum = PreSum()
    nums = [3,5,2,-2,4,1]
    k = 8
    result = pre_sum.leetcode_560(nums, k)
    print(result)