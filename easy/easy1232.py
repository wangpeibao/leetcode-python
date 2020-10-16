"""
1232. 缀点成线
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
示例 1：

输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true
示例 2：

输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false
提示：
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates 中不含重复的点
"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] == coordinates[0][0]:
            for coo in coordinates[2:]:
                if coo[0] != coordinates[0][0]:
                    return False
        else:
            for index, coo in enumerate(coordinates):
                if index in [0, 1]:
                    pass
                else:
                    if coo[0] == coordinates[index - 1][0]:
                        return False
                    else:
                        k1 = (coo[1] - coordinates[index - 1][1]) / (coo[0] - coordinates[index - 1][0])
                        k2 = (coordinates[index - 1][1] - coordinates[index - 2][1]) / (coordinates[index - 1][0] - coordinates[index - 2][0])
                        if k1 != k2:
                            return False
        return True

so = Solution()
print(so.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True)
print(so.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False)
print(so.checkStraightLine([[1,1], [2, 2], [2, 0]]) == False)