'''
5397. 最简分数  显示英文描述
给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  n 的 最简 分数 。分数可以以 任意 顺序返回
'''


class Solution:
    def simplifiedFractions(self, n: int):
        if n == 1 or n == 0:
            return []
        result = []
        has_in = set()
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if i / j in has_in:
                    continue
                result.append("%d/%d" % (i, j))
                has_in.add(i / j)
        return result


so = Solution()

print(so.simplifiedFractions(2) == ["1/2"])
print(so.simplifiedFractions(3) == ["1/2", "1/3", "2/3"])
print(so.simplifiedFractions(4) == ["1/2", "1/3", "1/4", "2/3", "3/4"])
print(so.simplifiedFractions(1) == [])
print(so.simplifiedFractions(6) == ["1/2", "1/3", "1/4", "1/5", "1/6", "2/3", "2/5", "3/4", "3/5", "4/5", "5/6"])
