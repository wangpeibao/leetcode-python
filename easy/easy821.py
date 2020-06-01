'''
821. 字符的最短距离
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
示例 1:
输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
说明:
字符串 S 的长度范围为 [1, 10000]。
C 是一个单字符，且保证是字符串 S 里的字符。
S 和 C 中的所有字母均为小写字母。
'''

from typing import List

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        cindex = [-10000]
        for index, ss in enumerate(S):
            if ss == C:
                cindex.append(index)
        cindex.append(10000)
        result = []
        for index, val in enumerate(S):
            for y, cc in enumerate(cindex):
                if cc > index:
                    result.append(min(cc - index, index - cindex[y - 1]))
                    break
        return result

so = Solution()

print(so.shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])
