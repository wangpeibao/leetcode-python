'''
884. 两句话中的不常见单词
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
返回所有不常用单词的列表。
您可以按任何顺序返回列表。
示例 1：
输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
示例 2：
输入：A = "apple apple", B = "banana"
输出：["banana"]
提示：
0 <= A.length <= 200
0 <= B.length <= 200
A 和 B 都只包含空格和小写字母。
'''

from typing import List

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:  # hash字典
        strA = A.split(" ")
        strB = B.split(" ")
        has_dict = dict()
        for a in strA:
            if a in has_dict.keys():
                has_dict[a] += 1
            else:
                has_dict[a] = 1
        for a in strB:
            if a in has_dict.keys():
                has_dict[a] += 1
            else:
                has_dict[a] = 1
        result = []
        for key, val in has_dict.items():
            if val == 1:
                result.append(key)
        return result

so = Solution()

print(so.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"])
print(so.uncommonFromSentences("apple apple", "banana") == ["banana"])