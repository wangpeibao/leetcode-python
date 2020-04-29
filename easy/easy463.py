'''
463. 岛屿的周长
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
示例 :

输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
输出: 16
解释: 它的周长是下面图片中的 16 个黄色的边：
'''


class Solution:
    def islandPerimeter(self, grid) -> int:  # DFS
        count = 0
        for xx, row in enumerate(grid):
            for yy, value in enumerate(row):
                if value == 1:
                    before = [(xx, yy)]
                    while before:
                        after = []
                        for x, y in before:
                            # 上下左右四个点,边界点
                            if x == 0:
                                count += 1
                            if y == 0:
                                count += 1
                            if x == len(grid) - 1:
                                count += 1
                            if y == len(row) - 1:
                                count += 1
                            # 中间点
                            if x > 0:
                                if grid[x - 1][y] == 1:
                                    after.append((x - 1, y))
                                if grid[x - 1][y] == 0:
                                    count += 1
                            if x < len(grid) - 1:
                                if grid[x + 1][y] == 1:
                                    after.append((x + 1, y))
                                if grid[x + 1][y] == 0:
                                    count += 1
                            if y > 0:
                                if grid[x][y - 1] == 1:
                                    after.append((x, y - 1))
                                if grid[x][y - 1] == 0:
                                    count += 1
                            if y < len(row) - 1:
                                if grid[x][y + 1] == 1:
                                    after.append((x, y + 1))
                                if grid[x][y + 1] == 0:
                                    count += 1
                            grid[x][y] = 2
                            before = list(set(after))
                    return count
        return count






so = Solution()

print(so.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16)
print(so.islandPerimeter([[1, 1], [1, 1]]) == 8)
