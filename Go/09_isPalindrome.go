package main

import (
	"fmt"
	"strconv"
)
//判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
//示例 1:
//输入: 121
//输出: true
//示例 2:
//输入: -121
//输出: false
//解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
//示例 3:
//输入: 10
//输出: false
//解释: 从右向左读, 为 01 。因此它不是一个回文数。

func isPalindrome(x int) bool {
	if x < 0 {
		return  false
	} else {
		str :=strconv.Itoa(x)
		y :=reverseString(str)
		if str == y {
			return  true
		} else {
			return  false
		}
	}
}


func reverseString(s string) string {
	runes := []rune(s)

	for from, to := 0, len(runes)-1; from < to; from, to = from + 1, to - 1 {
		runes[from], runes[to] = runes[to], runes[from]
	}

	return string(runes)
}

////直接在函数内 range判断
//func isPalindrome(x int) bool {
//	var str = strconv.Itoa(x)
//	if x < 0 {
//		return false
//	}
//	for i := range str{
//		if str[len(str)-1-i] != str[i] {
//			return false
//		}
//	}
//	return true
//}

func  main()  {
	 fmt.Println(isPalindrome(123341))
}

//执行结果： 通过
//显示详情 执行用时：20 ms, 在所有 Go 提交中击败了61.23%的用户
//内存消耗：5.6 MB, 在所有 Go 提交中击败了12.22%的用户