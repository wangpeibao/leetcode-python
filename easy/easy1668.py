"""
1668. 最大重复子字符串
给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，
那么单词 word 的 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。
如果 word 不是 sequence 的子串，那么重复值 k 为 0 。
给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。

示例 1：
输入：sequence = "ababc", word = "ab"
输出：2
解释："abab" 是 "ababc" 的子字符串。
示例 2：
输入：sequence = "ababc", word = "ba"
输出：1
解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
示例 3：
输入：sequence = "ababc", word = "ac"
输出：0
解释："ac" 不是 "ababc" 的子字符串。

提示：
1 <= sequence.length <= 100
1 <= word.length <= 100
sequence 和 word 都只包含小写英文字母。
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        index = 0
        offset = len(word)
        max_count = 0
        count = 0
        while index <= len(sequence) - offset:
            if sequence[index] == word[0] and sequence[index: index + offset] == word:
                count += 1
                index += offset
            else:
                max_count = max(max_count, count)
                count = 0
                index += 1
        return max(max_count, count)


so = Solution()
print(so.maxRepeating(sequence="ababc", word="ab") == 2)
print(so.maxRepeating(sequence="ababc", word="ba") == 1)
print(so.maxRepeating(sequence="ababc", word="ac") == 0)
print(so.maxRepeating(sequence="a", word="a") == 1)
