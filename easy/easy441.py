'''
441. 排列硬币
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
给定一个数字 n，找出可形成完整阶梯行的总行数。
n 是一个非负整数，并且在32位有符号整型的范围内。
示例 1:
n = 5
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.
示例 2:
n = 8
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
因为第四行不完整，所以返回3.
'''


class Solution:
    def arrangeCoins(self, n: int) -> int:  # 暴力破解法+二分法
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            mid_value = (mid + 1) * mid // 2
            if mid_value == n:
                return mid
            elif mid_value > n:
                end = mid
            else:
                start = mid
                if end - start == 1:
                    if (end + 1) * end // 2 > n:
                        return start
        return 0



so = Solution()

# print(so.arrangeCoins(1) == 1)
print(so.arrangeCoins(3) == 2)
print(so.arrangeCoins(5) == 2)
print(so.arrangeCoins(8) == 3)