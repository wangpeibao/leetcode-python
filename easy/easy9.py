'''
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # 负数肯定不是回文数
            return False
        result = 0
        stand = x
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10

        return result == stand


so = Solution()

print(so.isPalindrome(121) == True)
print(so.isPalindrome(-121) == False)
print(so.isPalindrome(10) == False)
print(so.isPalindrome(0) == True)
