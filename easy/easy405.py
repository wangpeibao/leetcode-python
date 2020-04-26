'''
405. 数字转换为十六进制数
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:
十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：
输入:
26
输出:
"1a"

示例 2：
输入:
-1
输出:
"ffffffff"
'''


class Solution:
    def toHex(self, num: int) -> str:
        stand = "0123456789abcdef"
        if num > 0:  # 当num大于0的时候，用除法取余得到十六进制
            result = ""
            while num > 0:
                result = stand[num % 16] + result
                num = num // 16
            return result
        elif num == 0:
            return "0"
        else:  # 负数特殊处理下，转成二进制
            result = []
            num = -num
            while num > 0:
                result = [int(stand[num % 2])] + result
                num = num // 2
            if len(result) <= 31:
                result = (31 - len(result)) * [0] + result
            else:
                return "80000000"
            result = result.copy()
            for i in range(31):
                if result[i] == 0:
                    result[i] = 1
                else:
                    result[i] = 0
            result = [1] + result
            index = 31
            jinwei = 1
            while index >= 0:
                if not jinwei:
                    break
                else:
                    if result[index] == 1:
                        jinwei = 1
                        result[index] = 0
                    else:
                        jinwei = 0
                        result[index] = 1
                index -= 1
            # 将二进制转十六进制
            record = ""
            for x in range(8):
                count = 0
                for y, value in enumerate(result[x * 4: x * 4 + 4]):
                    if y == 0:
                        count += value * 8
                    elif y == 1:
                        count += value * 4
                    elif y == 2:
                        count += value * 2
                    else:
                        count += value
                record += stand[count]
            return record





so = Solution()

print(so.toHex(26) == "1a")
print(so.toHex(-1) == "ffffffff")
print(so.toHex(-2) == "fffffffe")
print(so.toHex(-2147483648) == "80000000")
