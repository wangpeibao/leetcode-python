'''
643. 子数组最大平均数 I
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
示例 1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
注意:
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
'''


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:  # 滑块法
        start = 0
        end = k
        max_val = before_val = sum(nums[:k])
        while end < len(nums):
            self_val = before_val + nums[end] - nums[start]
            if self_val > max_val:
                max_val = self_val
            before_val = self_val
            start += 1
            end += 1
        return max_val / k


so = Solution()

print(so.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75)
