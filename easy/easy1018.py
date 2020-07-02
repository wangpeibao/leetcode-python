'''
1018. 可被 5 整除的二进制前缀
给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 True，否则为 False。
示例 1：
输入：[0,1,1]
输出：[True,False,False]
解释：
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
示例 2：
输入：[1,1,1]
输出：[False,False,False]
示例 3：
输入：[0,1,1,1,1,1]
输出：[True,False,False,False,True,False]
示例 4：
输入：[1,1,1,0,1]
输出：[False,False,False,False,False]
提示：
1 <= A.length <= 30000
A[i] 为 0 或 1
'''

from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        count = 0
        result = []
        for a in A:
            count = count * 2 + a
            if count % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result


so = Solution()

print(so.prefixesDivBy5([0, 1, 1]) == [True, False, False])
print(so.prefixesDivBy5([1, 1, 1]) == [False, False, False])
print(so.prefixesDivBy5([0, 1, 1, 1, 1, 1]) == [True, False, False, False, True, False])
print(so.prefixesDivBy5([1, 1, 1, 0, 1]) == [False, False, False, False, False])
