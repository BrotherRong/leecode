# -*- coding: utf-8 -*-
# @Time     : 2020/9/26 23:30
# @Author   : Rong
# @email    : mrrong0720@163.com
from typing import List

# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


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
print(s.nextPermutation([1,2,3]))