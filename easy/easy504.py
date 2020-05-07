'''
504. 七进制数
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        # 判断正负
        tag = "" if num >= 0 else "-"
        num = abs(num)
        # 转化成7进制
        result = ""
        while num >= 0:
            result = str(num % 7) + result
            num = num // 7
            if num == 0:
                break
        return tag + result

so = Solution()

print(so.convertToBase7(100) == "202")
print(so.convertToBase7(-7) == "-10")