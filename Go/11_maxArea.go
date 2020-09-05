package main

import "math"

// 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
// 说明：你不能倾斜容器，且 n 的值至少为 2。
// 示例：
// 输入：[1,8,6,2,5,4,8,3,7]
// 输出：49

func maxArea(height []int) int {
	i ,j ,res := 0, len(height)-1, 0
	for i < j {
		if height[i] < height[j] {
			res = int(math.Max(float64(res), float64(height[i]*(j-i))))
			i++
		} else {
			res = int(math.Max(float64(res), float64(height[j]*(j-i))))
			j--
		}
	}
	return res
}

func main() {
	var height = []int{1,8,6,2,5,4,8,3,7}
	println(maxArea(height))
}