'''
896. 单调数列
如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。
示例 1：
输入：[1,2,2,3]
输出：true
示例 2：
输入：[6,5,4,4]
输出：true
示例 3：
输入：[1,3,2]
输出：false
示例 4：
输入：[1,2,4,5]
输出：true
示例 5：
输入：[1,1,1]
输出：true
提示：
1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''

from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        status = None  # 是递增或递减
        for index, a in enumerate(A):
            if index != 0:
                if a == A[index - 1]:
                    pass
                elif a > A[index - 1]:
                    if status is None:
                        status = True
                    else:
                        if not status:
                            return False
                else:
                    if status is None:
                        status = False
                    else:
                        if status:
                            return False
        return True


so = Solution()
print(so.isMonotonic([1, 2, 2, 3]) == True)
print(so.isMonotonic([6, 5, 4, 4]) == True)
print(so.isMonotonic([1, 3, 2]) == False)
print(so.isMonotonic([1, 2, 4, 5]) == True)
print(so.isMonotonic([1, 1, 1]) == True)
