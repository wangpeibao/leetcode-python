'''
383. 赎金信
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)



注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

思路：　hash字典的方式处理
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = dict()
        for m in magazine:
            if m in m_dict.keys():
                m_dict[m] += 1
            else:
                m_dict[m] = 1
        for r in ransomNote:
            if r in m_dict.keys():
                if m_dict[r] > 0:
                    m_dict[r] -= 1
                else:
                    return False
            else:
                return False
        return True

so = Solution()

print(so.canConstruct("a", "b") == False)
print(so.canConstruct("aa", "ab") == False)
print(so.canConstruct("aa", "aab") == True)