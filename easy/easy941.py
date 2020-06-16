'''
941. 有效的山脉数组
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
示例 1：
输入：[2,1]
输出：false
示例 2：
输入：[3,5,5]
输出：false
示例 3：
输入：[0,3,2,1]
输出：true
提示：
0 <= A.length <= 10000
0 <= A[i] <= 10000
'''

from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        status = None  # 上升阶段
        for x in range(len(A) - 1):
            if status is None:
                if A[x] >= A[x + 1]:
                    return False
                else:
                    status = True
            if status:
                if A[x] > A[x + 1]:
                    status = False
                elif A[x] == A[x + 1]:
                    return False
            else:
                if A[x] <= A[x + 1]:
                    return False
        return False if status is None else True if not status else False

so = Solution()

print(so.validMountainArray([2, 1]) == False)
print(so.validMountainArray([3, 5, 5]) == False)
print(so.validMountainArray([0, 3, 2, 1]) == True)
print(so.validMountainArray([]) == False)