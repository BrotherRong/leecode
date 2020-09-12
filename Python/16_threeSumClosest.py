# -*- coding: utf-8 -*-
# @Time     : 2020/9/12 23:38
# @Author   : Rong
# @email    : mrrong0720@163.com

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 示例：
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 提示：
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()  # 排序
        ans = float('inf')

        for first in range(n - 2):  # 枚举第一个元素
            if first > 0 and nums[first] == nums[first - 1]: continue  # 保证first不会有重复

            second, third = first + 1, n - 1
            max_sum = nums[first] + nums[-2] + nums[-1]
            min_sum = nums[first] + nums[first + 1] + nums[first + 2]
            if max_sum <= target:  # 最大的数
                if abs(max_sum - target) < abs(ans - target):
                    ans = max_sum
                continue
            elif min_sum >= target:  # 最小的数
                if abs(min_sum - target) < abs(ans - target):
                    ans = min_sum
                break

            while second < third:
                two_sum_target = target - nums[first]
                s = nums[second] + nums[third]
                if abs(s + nums[first] - target) < abs(ans - target):
                    ans = s + nums[first]
                if s > two_sum_target:  # 当前数值太大 右指针左移
                    third -= 1
                    while third > second and nums[third] == nums[third + 1]:
                        third -= 1
                elif s < two_sum_target:  # 当前数值太小 左指针右移
                    second += 1
                    while third > second and nums[second] == nums[second - 1]:
                        second += 1
                else:  # 刚好等于 直接返回target即可
                    return target

        return ans
s = Solution()
print(s.threeSumClosest([-1,2,1,-4],1))