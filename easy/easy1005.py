'''
1005. K 次取反后最大化的数组和
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，
然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
以这种方式修改数组后，返回数组可能的最大和。
示例 1：
输入：A = [4,2,3], K = 1
输出：5
解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
示例 2：
输入：A = [3,-1,0,2], K = 3
输出：6
解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
示例 3：
输入：A = [2,-3,-1,5,-4], K = 2
输出：13
解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
提示：
1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
'''

from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:  # 分情况分析
        small_count = 0  # 得到小于0的个数
        zero_count = 0  # 零的根数
        count = 0  # 和
        abs_count = 0  # 绝对值和
        for a in A:
            count += a
            if a < 0:
                small_count += 1
                abs_count -= a
            elif a == 0:
                zero_count += 1
            else:
                abs_count += a
        if small_count >= K:  # 有大于等于K个的负数
            A.sort()
            for i in range(K):
                count += 2 * abs(A[i])
            return count
        else:
            if zero_count > 0:
                return abs_count
            else:
                if (K - small_count) % 2 == 0:
                    return abs_count
                else:
                    min_value = 101
                    for a in A:
                        if abs(a) < min_value:
                            min_value = abs(a)
                    return abs_count - 2 * min_value



so = Solution()

print(so.largestSumAfterKNegations([4, 2, 3], 1) == 5)
print(so.largestSumAfterKNegations([3, -1, 0, 2], 3) == 6)
print(so.largestSumAfterKNegations([2, -3, -1, 5, -4], 2) == 13)
