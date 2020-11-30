"""
1636. 按照频率将数组升序排序
给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。
请你返回排序后的数组。
示例 1：
输入：nums = [1,1,2,2,2,3]
输出：[3,1,1,2,2,2]
解释：'3' 频率为 1，'1' 频率为 2，'2' 频率为 3 。
示例 2：
输入：nums = [2,3,1,3,2]
输出：[1,3,3,2,2]
解释：'2' 和 '3' 频率都为 2 ，所以它们之间按照数值本身降序排序。
示例 3：
输入：nums = [-1,1,-6,4,5,-6,1,4,1]
输出：[5,-1,4,4,-6,-6,1,1,1]

提示：
1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_dict = {}
        for num in nums:
            if num in num_dict.keys():
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        # 转化成数组
        num_list = [[key, value] for key, value in num_dict.items()]
        num_list.sort(key=lambda a: (a[1], -a[0]))
        result = []
        for num_l in num_list:
            result += [num_l[0]] * num_l[1]
        return result


so = Solution()
print(so.frequencySort(nums=[1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2])
print(so.frequencySort(nums=[2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2])
print(so.frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1])
