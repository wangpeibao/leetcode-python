'''
949. 给定数字能组成的最大时间
给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
示例 1：
输入：[1,2,3,4]
输出："23:41"
示例 2：
输入：[5,5,5,5]
输出：""
提示：
A.length == 4
0 <= A[i] <= 9
'''

from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:  # 枚举所有符合条件的时间字符串
        A.sort()
        before = [[[a], set([index])] for index, a in enumerate(A)]
        for i in range(3):
            after = []
            for index, bb in enumerate(before):
                for y, a in enumerate(A):
                    if y not in bb[1]:
                        if i == 0:
                            if bb[0][0] * 10 + a < 24:
                                after.append([bb[0] + [a], bb[1] | set([y])])
                        elif i == 1:
                            if a < 6:
                                after.append([bb[0] + [a], bb[1] | set([y])])
                        else:
                            after.append([bb[0] + [a], bb[1] | set([y])])
            before = after
        if not before:
            return ""
        return f'{before[-1][0][0]}{before[-1][0][1]}:{before[-1][0][2]}{before[-1][0][3]}'





so = Solution()

print(so.largestTimeFromDigits([1, 2, 3, 4]) == "23:41")
print(so.largestTimeFromDigits([5, 5, 5, 5]) == "")
