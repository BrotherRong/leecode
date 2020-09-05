# -*- coding: utf-8 -*-
# @Time     : 2020/6/6 23:53
# @Author   : Rong
# @email    : mrrong0720@163.com
#
# 7. 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        abx = abs(x)
        sx = str(abx)
        if x > 0:
            sx = sx[::-1]
        else:
            sx = sx[::-1]
            sx = '-' + sx

        rev_int = int(sx)

        if rev_int <= 2 ** 31 - 1 and rev_int >= -(2 ** 31):
            return rev_int
        else:
            return 0
        
# test：
s = Solution()
print(s.reverse(-123))
