"""
1200. 最小绝对差
给你个整数数组 arr，其中每个元素都 不相同。
请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
示例 1：
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
示例 2：
输入：arr = [1,3,6,10,15]
输出：[[1,3]]
示例 3：
输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]
提示：
2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 解题思路，先排序，遍历，填充，更新
        result = []
        arr.sort()
        index = 0
        min_value = 2 * 10 ** 6 + 1
        while index < len(arr) - 1:
            if arr[index + 1] - arr[index] < min_value:
                min_value = arr[index + 1] - arr[index]
                result = [[arr[index], arr[index + 1]]]
            elif arr[index + 1] - arr[index] == min_value:
                result.append([arr[index], arr[index + 1]])
            index += 1
        return result


so = Solution()

print(so.minimumAbsDifference([4, 2, 1, 3]))
print(so.minimumAbsDifference([1, 3, 6, 10, 15]))
print(so.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
