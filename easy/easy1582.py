"""
1582. 二进制矩阵中的特殊位置
给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。
特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。
示例 1：
输入：mat = [[1,0,0],
            [0,0,1],
            [1,0,0]]
输出：1
解释：(1,2) 是一个特殊位置，因为 mat[1][2] == 1 且所处的行和列上所有其他元素都是 0
示例 2：
输入：mat = [[1,0,0],
            [0,1,0],
            [0,0,1]]
输出：3
解释：(0,0), (1,1) 和 (2,2) 都是特殊位置
示例 3：
输入：mat = [[0,0,0,1],
            [1,0,0,0],
            [0,1,1,0],
            [0,0,0,0]]
输出：2
示例 4：
输入：mat = [[0,0,0,0,0],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
输出：3
提示：
rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] 是 0 或 1
"""
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # 解题思路，计算出每行每列的值
        row_count = []
        col_count = [0 for _ in range(len(mat[0]))]
        for row in mat:
            row_count.append(sum(row))
            for index, value in enumerate(row):
                col_count[index] += value
        # 再次遍历
        count = 0
        for i, row in enumerate(mat):
            for j, value in enumerate(row):
                if value == 1 and row_count[i] == 1 and col_count[j] == 1:
                    count += 1
        return count


so = Solution()
print(so.numSpecial(mat=[[1, 0, 0],
                         [0, 0, 1],
                         [1, 0, 0]]) == 1)
print(so.numSpecial(mat=[[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]]) == 3)
print(so.numSpecial(mat=[[0, 0, 0, 1],
                         [1, 0, 0, 0],
                         [0, 1, 1, 0],
                         [0, 0, 0, 0]]) == 2)
print(so.numSpecial(mat=[[0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 0, 1, 1]]) == 3)
