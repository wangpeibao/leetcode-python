'''
476. 数字的补数
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

示例 1:
输入: 5
输出: 2
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2:
输入: 1
输出: 0
解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。

注意:
给定的整数保证在 32 位带符号整数的范围内。
你可以假定二进制数不包含前导零位。
本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/ 相同
'''

class Solution:
    def findComplement(self, num: int) -> int:  # 思路，二进制和十进制的相互转化问题
        bin_str = list(bin(num)[2:])
        for index, value in enumerate(bin_str):
            bin_str[index] = "1" if value == "0" else "0"
        # 计算求和
        count = 0
        level = 0
        for b in bin_str.__reversed__():
            count += 2 ** level * int(b)
            level += 1
        return count


so = Solution()

print(so.findComplement(5) == 2)
print(so.findComplement(1) == 0)

