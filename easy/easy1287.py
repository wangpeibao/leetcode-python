"""
1287. 有序数组中出现次数超过25%的元素
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
请你找到并返回这个整数

示例：
输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6

提示：
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        stand = len(arr) / 4
        count = 0
        before = None
        for a in arr:
            if a != before:
                count = 1
                before = a
            else:
                count += 1
            if count > stand:
                return a


so = Solution()
print(so.findSpecialInteger([1,2,2,6,6,6,6,7,10]) == 6)
print(so.findSpecialInteger([1,2,3,3]) == 3)