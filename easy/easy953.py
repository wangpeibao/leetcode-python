'''
953. 验证外星语词典
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。
示例 1：
输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
示例 2：
输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
输出：false
解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
示例 3：
输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false
解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。
提示：
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
在 words[i] 和 order 中的所有字符都是英文小写字母。
'''

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def _order_two_words(w1, w2):
            start1 = start2 = 0
            len1 = len(w1)
            len2 = len(w2)
            while start1 < len1 and start2 < len2:
                if w1[start1] == w2[start2]:
                    start1 += 1
                    start2 += 1
                else:  # 顺序
                    if order.index(w1[start1]) <= order.index(w2[start2]):
                        return True
                    else:
                        return False
            if start1 == len1 and start2 == len2:
                return True
            elif start1 == len1:
                return True
            else:
                return False

        for index, word in enumerate(words):
            if index != 0:
                if not _order_two_words(words[index - 1], word):
                    return False
        return True


so = Solution()

print(so.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True)
print(so.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") == False)
print(so.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") == False)
