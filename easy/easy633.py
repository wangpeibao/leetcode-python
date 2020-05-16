'''
633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5
示例2:
输入: 3
输出: False
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:  # 穷举法
        has_in = set()
        a = 0
        while a * a <= c:
            has_in.add(a * a)
            a += 1
        for ss in has_in:
            if c - ss in has_in:
                return True
        return False



so = Solution()

print(so.judgeSquareSum(5) == True)
print(so.judgeSquareSum(3) == False)