'''
7. 整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

class Solution:
    def reverse(self, x: int) -> int:
        # 将整数的反转问题转化成字符串的反转
        if x < 0:
            x_str = list(str(x)[1:])
            x_str.reverse()
            count = int("".join(x_str))
            if count > 2 ** 31:
                return 0
            return -count
        else:
            x_str = list(str(x))
            x_str.reverse()
            count = int("".join(x_str))
            if count > 2 ** 31 - 1:
                return 0
            return count

so = Solution()

examples = [
    {"x": 120, "result": 21},
    {"x": 123, "result": 321},
    {"x": -123, "result": -321}
]

for exa in examples:
    result = so.reverse(exa["x"])
    print(result == exa["result"])
