'''
541. 反转字符串 II
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        step = 0
        s = list(s)
        while True:
            start = 2 * k * step
            end = 2 * k * (step + 1)
            s_slice = s[start: end]
            if len(s_slice) >= k:
                for i in range(k // 2):
                    s[start + i], s[start + k - i - 1] = s[start + k - i - 1], s[start + i]
                step += 1
            else:
                for i in range((len(s) - start) // 2):
                    s[start + i], s[-1 - i] = s[-1 - i], s[start + i]
                break
        return "".join(s)


so = Solution()

print(so.reverseStr("abcdefg", 2) == "bacdfeg")
print(so.reverseStr("abcdefg", 8) == "gfedcba")
