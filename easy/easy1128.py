'''
1128. 等价多米诺骨牌对的数量
给你一个由一些多米诺骨牌组成的列表 dominoes。
如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。
示例：
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
提示：
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
'''


from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 和相等，差的绝对值相等
        has_dict = dict()
        for d1, d2 in dominoes:
            if (d1 + d2, abs(d1 - d2)) in has_dict.keys():
                has_dict[(d1 + d2, abs(d1 - d2))] += 1
            else:
                has_dict[(d1 + d2, abs(d1 - d2))] = 1
        count = 0
        for key, value in has_dict.items():
            count += value * (value - 1) // 2
        return count


so = Solution()


print(so.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]) == 1)