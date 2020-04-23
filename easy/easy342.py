'''
342. 4的幂
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
思路：不能循环不能递归，使用二进制来完成,最高位为１，其余低位只有偶数个0
'''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        num_bin = list(bin(num)[2:])
        if num_bin[0] == "1" and set(num_bin[1:]) == set("0") and len(num_bin[1:]) % 2 == 0:
            return True
        else:
            return False


so = Solution()

print(so.isPowerOfFour(16) == True)
print(so.isPowerOfFour(5) == False)
print(so.isPowerOfFour(2) == False)
