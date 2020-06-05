'''
面试题29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
'''

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        # 顺时针遍历
        x_start, x_end = 0, len(matrix) - 1
        if x_end == -1:
            return []
        y_start, y_end = 0, len(matrix[0]) - 1
        while x_start <= x_end and y_start <= y_end:
            for y in range(y_start, y_end + 1):
                result.append(matrix[x_start][y])
            for x in range(x_start + 1, x_end):
                result.append(matrix[x][y_end])
            if x_start != x_end:
                for y in range(y_end, y_start - 1, -1):
                    result.append(matrix[x_end][y])
            if y_start != y_end:
                for x in range(x_end - 1, x_start, -1):
                    result.append(matrix[x][y_start])
            x_start += 1
            y_start += 1
            x_end -= 1
            y_end -= 1
        return result



so = Solution()

print(so.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(so.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
print(so.spiralOrder([]) == [])
print(so.spiralOrder([[6, 9, 7]]) == [6, 9, 7])
