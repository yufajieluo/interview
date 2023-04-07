#!/usr/bin/python
# -*- coding:utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# @File: backTrack.py
# @Time: 2023/03/20 22:49:48
# @Author: WShuai.
# @License : (C)Copyright 2023 WShuai.

import copy
from typing import List

class BackTrack(object):
    def __init__(self) -> None:
        return
    
    def back_track_permute(self, nums: List[int], track: List[int], tracks: List[List[int]]):
        if len(track) == len(nums):
            current_track = copy.deepcopy(track)
            tracks.append(current_track)
        else:
            for value in nums:
                if value in track:
                    continue
                else:
                    track.append(value)
                    self.back_track_permute(nums, track, tracks)
                    track.remove(value)
                
        return tracks

    def leetcode_46(self, nums: List[int]) -> List[List[int]]:
        '''
        全排列 - 给定一个不含重复数字的数组 nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案
        '''
        result = []
        track = []
        self.back_track_permute(nums, track, result)
        return result

    def is_queen(self, track: List[str], row: int, col: int, n: int):
        result = True
        
        if result:
            for current_row in range(row):
                if track[current_row][col] == 'Q':
                    result = False
                    break

        if result:
            current_row = row
            current_col = col
            while current_row > 0 and current_col > 0:
                if track[current_row - 1][current_col - 1] == 'Q':
                    result = False
                    break
                current_row -= 1
                current_col -= 1

        if result:
            current_row = row
            current_col = col
            while current_row > 0 and current_col < n - 1:
                if track[current_row - 1][current_col + 1] == 'Q':
                    result = False
                    break
                current_row -= 1
                current_col += 1

        return result

    def back_track_queen(self, n: int, row: int, track: List[str], tracks: List[List[str]]):
        if row == n:
            current_track = copy.deepcopy(track)
            tracks.append(current_track)
        else:
            for col in range(n):
                if not self.is_queen(track, row, col, n):
                    continue
                else:
                    str = '{}{}{}'.format('.' * col, 'Q', '.' * (n - col - 1))
                    track.append(str)
                    self.back_track_queen(n, row + 1, track, tracks)
                    track.remove(str)

        return tracks

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        track = []
        self.back_track_queen(n, 0, track, result)
        return result



if __name__ == '__main__':
    back_track = BackTrack()
    nums = [1,2,3]
    print(back_track.solveNQueens(4))