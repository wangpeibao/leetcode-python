'''
1002. 查找常用字符
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。
示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：
输入：["cool","lock","cook"]
输出：["c","o"]
提示：
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
'''

from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        letter = set()
        let_count = dict()
        for aa in A[0]:
            if aa in letter:
                let_count[aa] += 1
            else:
                letter.add(aa)
                let_count[aa] = 1
        for a in A[1:]:
            l1 = set()
            l2 = dict()
            for aa in a:
                if aa in l1:
                    l2[aa] += 1
                else:
                    l1.add(aa)
                    l2[aa] = 1
            letter = letter & l1
            for l in letter:
                let_count[l] = min(let_count[l], l2[l])
        result = []
        for l in letter:
            for i in range(let_count[l]):
                result.append(l)
        return result

so = Solution()

print(so.commonChars(["bella", "label", "roller"]) == [["e", "l", "l"]])
print(so.commonChars(["cool", "lock", "cook"]) == ["c", "o"])
