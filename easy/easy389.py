'''
389. 找不同
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。
思路：　hash_dict处理方式
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = dict()
        for ss in s:
            if ss in s_dict.keys():
                s_dict[ss] += 1
            else:
                s_dict[ss] = 1
        for tt in t:
            if tt not in s_dict.keys():
                return tt
            if s_dict[tt] == 0:
                return tt
            s_dict[tt] -= 1
        return None

so = Solution()

print(so.findTheDifference("abcd", "abcde") == "e")
