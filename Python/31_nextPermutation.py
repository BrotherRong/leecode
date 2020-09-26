# -*- coding: utf-8 -*-
# @Time     : 2020/9/26 23:30
# @Author   : Rong
# @email    : mrrong0720@163.com
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                nums[i + 1:] = sorted(nums[i + 1:])
                return
        return nums.sort()




s = Solution()
print(s.nextPermutation([1,2,3,4,5]))