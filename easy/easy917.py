'''
917. 仅仅反转字母
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
示例 1：
输入："ab-cd"
输出："dc-ba"
示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
提示：
S.length <= 100
33 <= S[i].ASCIIcode <= 122
S 中不包含 \ or "
'''


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        start = 0
        end = len(S) - 1
        while start < end:
            if not (S[start] >= "a" and S[start] <= "z") and not (S[start] >= "A" and S[start] <= "Z"):
                start += 1
                continue
            if not (S[end] >= "a" and S[end] <= "z") and not (S[end] >= "A" and S[end] <= "Z"):
                end -= 1
                continue
            # 交换start 和 end
            S[start], S[end] = S[end], S[start]
            start += 1
            end -= 1
        return "".join(S)





so = Solution()

print(so.reverseOnlyLetters("ab-cd") == "dc-ba")
print(so.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba")
print(so.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!")
print(so.reverseOnlyLetters("7_28]") == "7_28]")