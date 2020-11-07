"""
1523. 在区间范围内统计奇数数目
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
示例 1：
输入：low = 3, high = 7
输出：3
解释：3 到 7 之间奇数数字为 [3,5,7] 。
示例 2：
输入：low = 8, high = 10
输出：1
解释：8 到 10 之间奇数数字为 [9] 。
提示：
0 <= low <= high <= 10^9
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 解题思路：数学归纳法，两个奇数：h - l // 2 + 1  两个偶数h -l // 2  h - l
        if low % 2 == high % 2 == 0:
            return (high - low) // 2
        elif low % 2 == high % 2 == 1:
            return (high - low) // 2 + 1
        else:
            return (high - low + 1) // 2


so = Solution()
print(so.countOdds(low=3, high=7) == 3)
print(so.countOdds(low=8, high=10) == 1)
print(so.countOdds(low=3, high=8) == 3)
