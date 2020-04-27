'''
434. 字符串中的单词数
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
'''

class Solution:
    def countSegments(self, s: str) -> int:  # 双指针法
        slow = 0
        count = 0
        length = len(s)
        while slow < length:
            if s[slow] == " ":
                slow += 1
            else:
                fast = slow + 1
                while fast <= length:
                    if fast == length:
                        count += 1
                        slow = fast
                        break
                    else:
                        if s[fast] == " ":
                            count += 1
                            slow = fast
                            break
                        else:
                            fast += 1
        return count



so = Solution()

print(so.countSegments("Hello, my name is John") == 5)