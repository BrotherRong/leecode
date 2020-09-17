# -*- coding: utf-8 -*-
# @Time     : 2020/9/17 12:44
# @Author   : Rong
# @email    : mrrong0720@163.com
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)

s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))


