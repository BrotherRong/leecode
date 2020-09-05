# -*- coding: utf-8 -*-
# @Time     : 2020/6/4 17:46
# @Author   : Rong
# @email    : mrrong0720@163.com

# 3. 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        if len_s == 0 :
            return 0
        set_s = set(s)

        max_len = len(set_s)
        max_sub_str = ""
        while max_len :
            if max_len == 1 :
                return 1
            i = 0
            while i + max_len <= len_s :
                sub_s = s[i:i+max_len]
                set_sub = set(sub_s)
                if len(set_sub) == len(sub_s) :
                    max_sub_str = sub_s
                    return (len(list(max_sub_str)))
                i = i+1
            max_len = max_len -1



    #通过	520 ms	12.9 MB	Python
    # 执行结果：
    # 通过
    # 显示详情
    # 执行用时:
    # 520
    # ms
    # , 在所有
    # Python
    # 提交中击败了
    # 16.34 %
    # 的用户
    # 内存消耗:
    # 12.9
    # MB
    # , 在所有
    # Python
    # 提交中击败了
    # 15.15 %
    # 的用户
    res = lengthOfLongestSubstring('','pwwkew')
    print(res)
