'''
680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
示例 1:
输入: "aba"
输出: True
示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        status = False
        status1 = True
        status2 = True
        while start < end:
            if s[start] != s[end]:
                if status:
                    status1 = False
                    break
                else:
                    status = True
                    start += 1
            else:
                start += 1
                end -= 1
        start = 0
        end = len(s) - 1
        status = False
        while start < end:
            if s[start] != s[end]:
                if status:
                    status2 = False
                    break
                else:
                    status = True
                    end -= 1
            else:
                start += 1
                end -= 1
        return status1 or status2

so = Solution()

print(so.validPalindrome("aba") == True)
print(so.validPalindrome("abca") == True)
print(so.validPalindrome("abc") == False)
