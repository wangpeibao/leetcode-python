'''
867. 转置矩阵
给定一个矩阵 A， 返回 A 的转置矩阵。
矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
示例 1：
输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：
输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
提示：
1 <= A.length <= 1000
1 <= A[0].length <= 1000

'''

from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = [[] for i in range(len(A[0]))]
        for row in A:
            for y, val in enumerate(row):
                result[y].append(val)
        return result

so = Solution()

print(so.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
print(so.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]])
