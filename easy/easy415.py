'''
415. 字符串相加
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        x = len(num1) - 1
        y = len(num2) - 1
        c = 0
        while x >= 0 or y >= 0:
            a = int(num1[x]) if x >= 0 else 0
            b = int(num2[y]) if y >= 0 else 0
            self_reuslt = a + b + c
            result = str(self_reuslt % 10) + result
            c = self_reuslt // 10
        if c == 1:
            result = "1" + result
        return result
