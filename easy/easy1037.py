'''
1037. 有效的回旋镖
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
示例 1：
输入：[[1,1],[2,3],[3,2]]
输出：true
示例 2：
输入：[[1,1],[2,2],[3,3]]
输出：false
提示：
points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
'''

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 各个点不相同
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        # 如果前两个点组成的直线垂直于x轴
        if points[0][0] == points[1][0]:
            if points[2][0] != points[0][0]:
                return True
            else:
                return False
        else:
            if points[1][0] == points[2][0]:
                if points[0][0] != points[1][0]:
                    return True
                else:
                    return False
            else:
                if (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) == (points[2][1] - points[1][1]) / (points[2][0] - points[1][0]):
                    return False
                else:
                    return True

so = Solution()

print(so.isBoomerang([[1,1],[2,3],[3,2]]) == True)
print(so.isBoomerang([[1,1],[2,2],[3,3]]) == False)