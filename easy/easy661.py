'''
661. 图片平滑器
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，
平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
示例 1:
输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
注意:
给定矩阵中的整数范围为 [0, 255]。
矩阵的长和宽的范围均为 [1, 150]。
'''


class Solution:
    def imageSmoother(self, M):  # 暴力破解法
        result = []
        lenx = len(M)
        leny = len(M[0])
        for x, row in enumerate(M):
            result.append([])
            for y, val in enumerate(row):
                count = 1
                values = val
                if y > 0:
                    count += 1
                    values += M[x][y - 1]
                if y < leny - 1:
                    count += 1
                    values += M[x][y + 1]
                if x > 0:
                    count += 1
                    values += M[x - 1][y]
                    if y > 0:
                        count += 1
                        values += M[x - 1][y - 1]
                    if y < leny - 1:
                        count += 1
                        values += M[x - 1][y + 1]
                if x < lenx - 1:
                    count += 1
                    values += M[x + 1][y]
                    if y > 0:
                        count += 1
                        values += M[x + 1][y - 1]
                    if y < leny - 1:
                        count += 1
                        values += M[x + 1][y + 1]
                result[x].append(values//count)
        return result


so = Solution()

# print(so.imageSmoother([[1, 1, 1],
#                         [1, 0, 1],
#                         [1, 1, 1]]))
print(so.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
