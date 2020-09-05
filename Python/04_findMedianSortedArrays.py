# -*- coding: utf-8 -*-
# @Time     : 2020/6/6 19:54
# @Author   : Rong
# @email    : mrrong0720@163.com

# 寻找两个正序数组的中位数
# 给定两个大小为m和n
# 的正序（从小到大）数组 nums1和nums2。
#
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为
# O(log(m + n))。
#
# 你可以假设 nums1 和nums2 不会同时为空。
#
# 示例1:
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是(2 + 3) / 2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        len_num = len(nums1)
        mid_num = int(len_num/2)
        if(len_num%2==1):
            return nums1[mid_num]
        else:
            return (nums1[mid_num - 1] + nums1[mid_num])/2
    # 通过44 ms 13.1 MB Python

        nums = nums1 + nums2
        nums.sort()
        size = len(nums)

        if size % 2 == 1:
            return nums[size // 2]

        if size % 2 == 0:
            return (nums[size // 2] + nums[size // 2 - 1]) / 2

    res = findMedianSortedArrays('',[1, 3],[2,4])
    print(res)
