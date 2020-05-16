'''
5399. 数位成本和为目标值的最大数字
题目难度 Hard
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：

给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
总成本必须恰好等于 target 。
添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。
如果按照上述要求无法得到任何整数，请你返回 "0"
'''


class Solution:
    def largestNumber(self, cost, target: int) -> str:

        def str_max(slist):
            max_value = ""
            for s in slist:
                if len(s) > len(max_value):
                    max_value = s
                elif len(s) == len(max_value):
                    for i in range(len(s)):
                        if s[i] > max_value[i]:
                            max_value = s
                            break
                        elif s[i] < max_value[i]:
                            break
            return max_value


        dp = [""] * (target + 1)
        dp = dp.copy()
        for i in range(1, target + 1):
            mid_result = []
            for k, v in enumerate(cost):
                if v == i:
                    mid_result.append(str(k + 1))
            for j in range(1, i):
                if not dp[j]:
                    continue
                else:
                    if dp[i - j]:
                        mid_result.append(dp[j] + dp[i - j])
            if mid_result:
                dp[i] = str_max(mid_result)
        return dp[-1] if dp[-1] else "0"


so = Solution()

print(so.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9) == "7772")
print(so.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12) == "85")
print(so.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5) == "0")
print(so.largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], 47) == "32211")
