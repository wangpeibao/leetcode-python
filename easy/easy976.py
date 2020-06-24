'''
976. 三角形的最大周长
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。
示例 1：
输入：[2,1,2]
输出：5
示例 2：
输入：[1,2,1]
输出：0
示例 3：
输入：[3,2,3,4]
输出：10
示例 4：
输入：[3,6,2,3]
输出：8

提示：
3 <= A.length <= 10000
1 <= A[i] <= 10^6
'''

from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:  # 根据三角形特性，两边之和大于第三边
        A.sort(reverse=True)
        end = 2
        length = len(A)
        while end < length:
            if A[end] + A[end - 1] > A[end - 2]:
                return A[end] + A[end - 1] + A[end - 2]
            end += 1
        return 0


so = Solution()

print(so.largestPerimeter([2, 1, 2]) == 5)
print(so.largestPerimeter([1, 2, 1]) == 0)
print(so.largestPerimeter([3, 2, 3, 4]) == 10)
print(so.largestPerimeter([3, 6, 2, 3]) == 8)
