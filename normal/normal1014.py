'''
1014. 最佳观光组合
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
返回一对观光景点能取得的最高分。
示例：
输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
提示：
2 <= A.length <= 50000
1 <= A[i] <= 1000
'''

from typing import List


class Solution:
    def maxScoreSightseeingPair1(self, A: List[int]) -> int:  # 暴力破解法(会超时)
        length = len(A)
        count = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                self_count = A[i] + A[j] + i - j
                if self_count > count:
                    count = self_count
        return count

    def maxScoreSightseeingPair(self, A: List[int]) -> int:  # 将公式拆分A[i] + i 和 A[j] - j
        count = 0
        before = A[0] + 0
        for j in range(1, len(A)):
            count = max(count, before + A[j] - j)
            before = max(before, A[j] + j)
        return count




so = Solution()

print(so.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11)
