'''
718. 最长重复子数组
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
示例 1:
输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]
说明:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''

from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:  # 滑动窗口法
        astart = 0
        lena = len(A)
        lenb = len(B)
        result = 0
        while lena - astart >= result:
            bindex = 0
            aindex = astart
            before = None
            while bindex < lenb and aindex < lena:
                if A[aindex] != B[bindex]:
                    before = None
                else:
                    if before is not None:
                        if aindex - before + 1 > result:
                            result = aindex - before + 1
                    else:
                        before = aindex
                        if result == 0:
                            result = 1
                aindex += 1
                bindex += 1
            astart += 1
        bstart = 0
        while lenb - bstart >= result:
            bindex = bstart
            aindex = 0
            before = None
            while bindex < lenb and aindex < lena:
                if A[aindex] != B[bindex]:
                    before = None
                else:
                    if before is not None:
                        if bindex - before + 1 > result:
                            result = bindex - before + 1
                    else:
                        before = bindex
                        if result == 0:
                            result = 1
                aindex += 1
                bindex += 1
            bstart += 1
        return result



so = Solution()

print(so.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3)
