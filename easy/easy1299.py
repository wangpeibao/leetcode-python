"""
1299. 将每个元素替换为右侧最大元素
给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。
完成所有替换操作后，请你返回这个数组。

示例：
输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]

提示：
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 转换思路，从右向左，依次替换成当前最大元素
        max_value = -1
        index = len(arr) - 1
        while index >= 0:
            temp_value = arr[index]
            arr[index] = max_value
            max_value = max(max_value, temp_value)
            index -= 1
        return arr


so = Solution()
print(so.replaceElements([17,18,5,4,6,1]))
