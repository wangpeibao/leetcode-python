'''
905. 按奇偶排序数组
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
你可以返回满足此条件的任何数组作为答案。
示例：
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
提示：
1 <= A.length <= 5000
0 <= A[i] <= 5000
'''

from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # 双指针交换
        start = 0
        length = len(A)
        end = length - 1
        while start < end:
            if A[start] % 2 == 0:
                start += 1
            else:
                if A[end] % 2 == 1:
                    end -= 1
                else:
                    A[start], A[end] = A[end], A[start]
                    start += 1
                    end -= 1
        return A


so = Solution()

print(so.sortArrayByParity([3,1,2,4]) == [2,4,3,1])