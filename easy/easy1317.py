"""
1317. 将整数转换为两个无零整数的和
「无零整数」是十进制表示中 不含任何 0 的正整数。
给你一个整数 n，请你返回一个 由两个整数组成的列表 [A, B]，满足：
A 和 B 都是无零整数
A + B = n
题目数据保证至少有一个有效的解决方案。
如果存在多个有效解决方案，你可以返回其中任意一个。

示例 1：
输入：n = 2
输出：[1,1]
解释：A = 1, B = 1. A + B = n 并且 A 和 B 的十进制表示形式都不包含任何 0 。
示例 2：
输入：n = 11
输出：[2,9]
示例 3：
输入：n = 10000
输出：[1,9999]
示例 4：
输入：n = 69
输出：[1,68]
示例 5：
输入：n = 1010
输出：[11,999]

提示：
2 <= n <= 10^4
"""
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # 思路：要想a,b之中没有零，则a中对应位没有和n相同的，用加法的思路处理
        stand = []
        while n > 0:
            stand.append(n % 10)
            n = n // 10
        A = 0
        B = 0
        j = 0
        for index, s in enumerate(stand):
            if index == len(stand) - 1:
                if s - j == 0:
                    break
                elif s - j == 1:
                    A += 10 ** index
                    break
            for a in range(1, 10):
                b = s - j - a
                if b < 0:
                    b = s + 10 - j - a
                    j = 1
                    if b != 0:
                        A += a * (10 ** index)
                        B += b * (10 ** index)
                        break
                elif b > 0:
                    A += a * (10 ** index)
                    B += b * (10 ** index)
                    j = 0
                    break
        return [A, B]



so = Solution()
print(so.getNoZeroIntegers(160))
print(so.getNoZeroIntegers(1010))
print(so.getNoZeroIntegers(10000))
print(so.getNoZeroIntegers(69))
print(so.getNoZeroIntegers(2))
print(so.getNoZeroIntegers(11))
print(so.getNoZeroIntegers(160))
