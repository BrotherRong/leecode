# -*- coding: utf-8 -*-
# @Time     : 2020/6/6 22:26
# @Author   : Rong
# @email    : mrrong0720@163.com

# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        while True:
            i = 0
            while i + len_s  <= len(s):
                sl = s[i:i+len_s]
                sr = sl[::-1]
                if sl == sr:
                    return sl
                i = i+1
            len_s = len_s - 1
            if len_s == 0:
                return "No solution"

    test_str = "abcbd"
    print(longestPalindrome('',test_str))