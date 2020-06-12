'''
922. 按奇偶排序数组 II
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。
示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
提示：
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''

from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # 双指针
        start = 0
        length = len(A)
        while start < length:
            if (start % 2 == 0 and A[start] % 2 == 0) or (start % 2 == 1 and A[start] % 2 == 1):
                start += 1
                continue
            # 处理找到下个不符合的
            end = start + 1
            while end < length:
                if (end % 2 == 0 and A[end] % 2 == 0) or (end % 2 == 1 and A[end] % 2 == 1):
                    end += 2
                else:
                    A[start], A[end] = A[end], A[start]
                    start = start + 2
        return A



so = Solution()

print(so.sortArrayByParityII([4,2,5,7]) == [4,5,2,7])