'''
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。
示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''

from typing import List


class Solution:
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:  # 广度优先搜索(会超时)
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])
        count = 0
        before = [[0, 0]]
        index = 0
        while before:
            after = []
            print(index, before)
            index += 1
            for x, y in before:
                if obstacleGrid[x][y] != 1:
                    if x == m - 1 and y == n - 1:
                        count += 1
                    else:
                        if x < m - 1:
                            if obstacleGrid[x + 1][y] != 1:
                                after.append([x + 1, y])
                        if y < n - 1:
                            if obstacleGrid[x][y + 1] != 1:
                                after.append([x, y + 1])
            before = set(after)
        return count

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:  # 动态规划，对于一个点a[x][y], 路径数是起点到它的路径数*它到终点的路径数
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])
        has_dict = {(0, 0): (obstacleGrid[0][0] + 1) % 2}
        for x in range(m):
            for y in range(n):
                if (x, y) in has_dict.keys():
                    if x + 1 < m:
                        if obstacleGrid[x + 1][y] == 0:
                            if (x + 1, y) in has_dict.keys():
                                has_dict[(x + 1, y)] += has_dict[(x, y)]
                            else:
                                has_dict[(x + 1, y)] = has_dict[(x, y)]
                        else:
                            has_dict[(x + 1, y)] = 0
                    if y + 1 < n:
                        if obstacleGrid[x][y + 1] == 0:
                            if (x, y + 1) in has_dict.keys():
                                has_dict[(x, y + 1)] += has_dict[(x, y)]
                            else:
                                has_dict[(x, y + 1)] = has_dict[(x, y)]
                        else:
                            has_dict[(x, y + 1)] = 0
        return has_dict[(m - 1, n - 1)]



so = Solution()

print(so.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]) == 2)
print(so.uniquePathsWithObstacles([[0]]) == 1)
print(so.uniquePathsWithObstacles([[1]]) == 0)
print(so.uniquePathsWithObstacles(
    [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]) == 1)
