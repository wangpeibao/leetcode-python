'''
5394. 对角线遍历 II  显示英文描述
题目难度 Medium
给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。
示例 1：
输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,4,2,7,5,3,8,6,9]
示例 2：

输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
示例 3：

输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
输出：[1,4,2,5,3,8,6,9,7,10,11]
示例 4：

输入：nums = [[1,2,3,4,5,6]]
输出：[1,2,3,4,5,6]

提示：

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
nums 中最多有 10^5 个数字。
'''


class Solution:
    def findDiagonalOrder1(self, nums):  # 边界点方法(时间超限)
        status = True
        level = 0
        result = []
        max_row = len(nums)
        while status:
            status = False
            x = level
            y = 0
            while x >= 0:
                if x < max_row and y < len(nums[x]):
                    result.append(nums[x][y])
                    status = True
                x -= 1
                y += 1
            level += 1
        return result

    def findDiagonalOrder(self, nums):  # 对角线hashdict
        has_dict = dict()
        for x, row in enumerate(nums):
            for y, value in enumerate(row):
                if x + y in has_dict.keys():
                    has_dict[x + y] = [value] + has_dict[x + y]  # 注意这里有一个反序
                else:
                    has_dict[x + y] = [value]
        start = 0
        result = []
        while start in has_dict.keys():
            result += has_dict[start]
            start += 1
        return result



so = Solution()

print(so.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

print(so.findDiagonalOrder([[1, 2, 3, 4, 5, 6]]))
print(so.findDiagonalOrder([[14, 12, 19, 16, 9], [13, 14, 15, 8, 11], [11, 13, 1]]) == [14, 13, 12, 11, 14, 19, 13, 15,
                                                                                        16, 1, 8, 9, 11])
