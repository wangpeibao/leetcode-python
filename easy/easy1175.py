"""
1175. 质数排列
请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。

示例 1：
输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
示例 2：
输入：n = 100
输出：682289015
提示：
1 <= n <= 100
"""


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # 解题思路：找到小于等于n的质数的个数m,则答案为 m! * (n - 3)!
        # 大于1，除了1和它本身，再也没有别的除数
        m = 0
        stand = 10 ** 9 + 7
        for num in range(2, n + 1):
            status = True
            for div in range(2, num):
                if div * div > num:
                    break
                if num % div == 0:
                    status = False
                    break
            if status:
                m += 1
        result = 1
        for i in range(2, m + 1):
            result = (i * result) % stand
        for i in range(2, n - m + 1):
            result = (i * result) % stand
        return result

so = Solution()
print(so.numPrimeArrangements(5) == 12)
print(so.numPrimeArrangements(100) == 682289015)
