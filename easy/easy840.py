'''
840. 矩阵中的幻方
3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
示例：
输入: [[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]
输出: 1
解释:
下面的子矩阵是一个 3 x 3 的幻方：
438
951
276
而这一个不是：
384
519
762
总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
提示:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
'''

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:  # 根据题意，其和是15
        lenrow = len(grid)
        lencol = len(grid[0])
        count = 0
        stand = set([(1, 5, 9), (1, 6, 8), (2, 4, 9), (2, 5, 8), (2, 6, 7), (3, 4, 8), (3, 5, 7), (4, 5, 6)])
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if x + 2 < lenrow and y + 2 < lencol:
                    status1 = True
                    for i in range(3):
                        a = [grid[x + i][y], grid[x + i][y + 1], grid[x + i][y + 2]]
                        a.sort()
                        if tuple(a) not in stand:
                            status1 = False
                            break
                        b = [grid[x][y + i], grid[x + 1][y + i], grid[x + 2][y + i]]
                        b.sort()
                        if tuple(b) not in stand:
                            status1 = False
                            break
                    if status1:
                        a = [grid[x][y], grid[x + 1][y + 1], grid[x + 2][y + 2]]
                        a.sort()
                        b = [grid[x + 2][y], grid[x + 1][y + 1], grid[x][y + 2]]
                        b.sort()
                        if tuple(a) in stand and tuple(b) in stand:
                            count += 1
        return count


so = Solution()

print(so.numMagicSquaresInside([[4, 3, 8, 4],
                                [9, 5, 1, 9],
                                [2, 7, 6, 2]]) == 1),
print(so.numMagicSquaresInside([[2, 7, 6], [1, 5, 9], [4, 3, 8]]) == 0)
