# -*- coding: utf-8 -*-
# @Time     : 2020/9/6 23:55
# @Author   : Rong
# @email    : mrrong0720@163.com


class Solution:
    def romanToInt(self, s: str) -> int:
        Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Int = 0
        n = len(s)

        for index in range(n - 1):
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
                Int -= Roman2Int[s[index]]
            else:
                Int += Roman2Int[s[index]]

        return Int + Roman2Int[s[-1]]


s = Solution()
print(s.romanToInt("III"))