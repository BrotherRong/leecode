<?php
/**
 * Created by PhpStorm.
 * User: rongxiang
 * Date: 2020/9/4
 * Time: 15:57
 */

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

class Solution {
    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        if($x<0){
            return false;
        }
        else{
            $y = strrev($x);
            if($x == $y){
                return true;
            }
            else {
                return false;
            }
        }
    }
}