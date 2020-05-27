'''
784. 字母大小写全排列
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
输入: S = "3z4"
输出: ["3z4", "3Z4"]
输入: S = "12345"
输出: ["12345"]
注意：
S 的长度不超过12。
S 仅由数字和字母组成。
'''

from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:  # 广度优先搜索
        before = []
        for s in S:
            if not before:
                if s >= "a" and s <= "z":
                    before.append(s.upper())
                if s >= "A" and s <= "Z":
                    before.append(s.lower())
                before.append(s)
            else:
                after = []
                if s >= "a" and s <= "z":
                    for bb in before:
                        after.append(bb + s.upper())
                if s >= "A" and s <= "Z":
                    for bb in before:
                        after.append(bb + s.lower())
                for bb in before:
                    after.append(bb + s)
                before = after
        return before



so = Solution()

print(so.letterCasePermutation("a1b2") == [["a1b2", "a1B2", "A1b2", "A1B2"]])
print(so.letterCasePermutation("3z4") == ["3z4", "3Z4"])
print(so.letterCasePermutation("12345") == ["12345"])