# -*- coding: utf-8 -*-
# @Time     : 2020/9/4 15:48
# @Author   : Rong
# @email    : mrrong0720@163.com

#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 示例 1:
# 输入: 121
# 输出: true
# 示例 2:
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
           return False
        else :
            y = str(x)[::-1]
            # y = ''.join(reversed(str(x)))    #两种字符串翻转方法
            if y == str(x) :
                return True
            else :
                return False

# test：
s = Solution()
print(s.isPalindrome(12321))