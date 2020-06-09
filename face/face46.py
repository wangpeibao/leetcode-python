'''
面试题46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
提示：
0 <= num < 231
'''


class Solution:
    def translateNum(self, num: int) -> int:  # 广度优先搜索
        num = str(num)
        length = len(num)
        before = [[0]]
        count = 0
        while before:
            after = []
            for start in before:
                if start[-1] < length:
                    after.append(start + [start[-1] + 1])
                    if start[-1] + 1 < length and num[start[-1]] != "0" and int(num[start[-1]: start[-1] + 2]) <= 25:
                        after.append(start + [start[-1] + 2])
                else:
                    count += 1
            before = after
        return count


so = Solution()

print(so.translateNum(12258) == 5)