'''
1137. 第 N 个泰波那契数
泰波那契序列 Tn 定义如下：
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
示例 1：
输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：
输入：n = 25
输出：1389537
提示：
0 <= n <= 37
答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
'''


class Solution:
    def tribonacci(self, n: int) -> int:
        stand = [0, 1, 1]
        if n <= 2:
            return stand[n]
        for i in range(n-2):
            stand.append(stand[i] + stand[i + 1] + stand[i + 2])
        return stand[-1]


so =Solution()

print(so.tribonacci(4) == 4)
print(so.tribonacci(25) == 1389537)