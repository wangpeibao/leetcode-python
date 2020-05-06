'''
500. 键盘行
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

American keyboard

示例：
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
注意：
你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。
'''

class Solution:
    def findWords(self, words):
        s1 = set(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"])
        s2 = set(["a", "s", "d", "f", "g", "h", "j", "k", "l"])
        s3 = set(["z", "x", "c", "v", "b", "n", "m"])
        result = []
        for word in words:
            if word:
                if word[0].lower() in s1:
                    status = True
                    for w in word:
                        if w.lower() not in s1:
                            status = False
                            break
                    if status:
                       result.append(word)
                if word[0].lower() in s2:
                    status = True
                    for w in word:
                        if w.lower() not in s2:
                            status = False
                            break
                    if status:
                        result.append(word)
                if word[0].lower() in s3:
                    status = True
                    for w in word:
                        if w.lower() not in s3:
                            status = False
                            break
                    if status:
                        result.append(word)
        return result


so = Solution()


print(so.findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"])