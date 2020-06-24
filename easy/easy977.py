'''
977. 有序数组的平方
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
'''

from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sorta = []
        sortb = []
        for index, val in enumerate(A):
            if val < 0:
                sorta = [abs(val)] + sorta
            else:
                sortb = A[index:]
                break
        # 合并两个有序数列
        result = []
        start1, start2 = 0, 0
        len1 = len(sorta)
        len2 = len(sortb)
        while start1 < len1 or start2 < len2:
            if start1 < len1 and start2 < len2:
                if sorta[start1] <= sortb[start2]:
                    result.append(sorta[start1] ** 2)
                    start1 += 1
                else:
                    result.append(sortb[start2] ** 2)
                    start2 += 1
            else:
                if start1 < len1:
                    result.append(sorta[start1] ** 2)
                    start1 += 1
                else:
                    result.append(sortb[start2] ** 2)
                    start2 += 1
        return result


so = Solution()

print(so.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100])
print(so.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121])
