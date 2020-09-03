# -*- coding: utf-8 -*-
# @Time     : 2020/6/4 17:07
# @Author   : Rong
# @email    : mrrong0720@163.com

# 1. 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#  
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and i < j:
                    if target == nums[i] + nums[j]:
                        return [i, j]
                    else:
                        continue
                else:
                    continue
        #通过	6444 ms	13.4 MB	Python

        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return "No solution here!"
            r = target - nums[i]
            # Can't use a num twice
            num_follow = nums[i + 1:]
            if r in num_follow:
                return [i, num_follow.index(r) + i + 1]
            i = i + 1

        # 通过 688 ms	13.4 MB	Python

        for i in range(len(nums) - 1):
            if i == len(nums) - 1:
                return "No solution here!"
            r = target - nums[i]
            # Can't use a num twice
            num_follow = nums[i + 1:]
            if r in num_follow:
                return [i, num_follow.index(r) + i + 1]

        # 通过 700 ms	13.4 MB	Python


