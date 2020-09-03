# -*- coding: utf-8 -*-
# @Time     : 2020/6/4 17:23
# @Author   : Rong
# @email    : mrrong0720@163.com

# 2. 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = l1
        i = 1
        num_l1 = 0
        # get num of l1
        while n:
            num_l1 = num_l1 + n.val * i
            i = i * 10
            n = n.next

        m = l2
        j = 1
        num_l2 = 0
        # get num of l2
        while m:
            num_l2 = num_l2 + m.val * j
            j = j * 10
            m = m.next

        str_num = str(num_l1 + num_l2)
        str_num = str_num[::-1]
        res = list_result = ListNode(0)

        for s in str_num:
            list_result.next = ListNode(int(s))
            list_result = list_result.next
        return res.next

    # 	通过	68 ms	12.7 MB	Python


    addTwoNumbers(0, [2, 4, 3], [5, 6, 4])

