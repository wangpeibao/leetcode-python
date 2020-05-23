'''
697. 数组的度
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
示例 1:
输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:
输入: [1,2,2,3,1,4,2]
输出: 6
注意:
nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。
'''

from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 找到最大的度以及其数值
        num_dict = dict()
        max_count = 1
        for index, num in enumerate(nums):
            if num in num_dict.keys():
                num_dict[num][0] += 1
                max_count = num_dict[num][0] if num_dict[num][0] > max_count else max_count
                num_dict[num][2] = index
            else:
                num_dict[num] = [1, index, index]
        min_length = 50001
        for key, val in num_dict.items():
            if val[0] == max_count:
                min_length = val[2] - val[1] if val[2] - val[1] < min_length else min_length
        return min_length + 1

so = Solution()

print(so.findShortestSubArray([1, 2, 2, 3, 1]) == 2)
print(so.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6)
print(so.findShortestSubArray([1]) == 1)
