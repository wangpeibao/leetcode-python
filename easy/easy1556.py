"""
1556. 千位分隔数
给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。
示例 1：
输入：n = 987
输出："987"
示例 2：
输入：n = 1234
输出："1.234"
示例 3：
输入：n = 123456789
输出："123.456.789"
示例 4：
输入：n = 0
输出："0"
提示：
0 <= n < 2^31
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        nstr = str(n)
        length = len(nstr)
        result = ""
        for index in range(length):
            if index % 3 == 0 and index != 0:
                result = nstr[length - 1 - index] + "." + result
            else:
                result = nstr[length - 1 - index] + result
        return result


so = Solution()
print(so.thousandSeparator(n=987) == "987")
print(so.thousandSeparator(n=1234) == "1.234")
print(so.thousandSeparator(n=123456789) == "123.456.789")
