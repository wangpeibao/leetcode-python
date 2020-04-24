'''
401. 二进制手表
二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。

例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

案例:

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]


注意事项:

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。

思路：　暴力破解法，枚举所有的可能
'''

class Solution:
    def readBinaryWatch(self, num: int):
        result = []
        if num == 0:
            return ["0:00"]
        for x in range(10):
            if not result:
                result.append({"string": [0], "count": 0})
                result.append({"string": [1], "count": 1})
            else:
                after = []
                for rr in result:
                    if rr["count"] >= num:
                        after.append({"string": rr["string"] + [0], "count": rr["count"]})
                    else:
                        if num - rr["count"] == 10 - x:
                            after.append({"string": rr["string"] + [1], "count": rr["count"] + 1})
                        else:
                            after.append({"string": rr["string"] + [0], "count": rr["count"]})
                            after.append({"string": rr["string"] + [1], "count": rr["count"] + 1})
                result = after
        # 对于所有的结果处理
        record = []
        for rr in result:
            hour = rr["string"][0] * 8 + rr["string"][1] * 4 + rr["string"][2] * 2 + rr["string"][3] * 1
            if hour > 11:
                continue
            minute = rr["string"][4] * 32 + rr["string"][5] * 16 + rr["string"][6] * 8 + rr["string"][7] * 4 + \
                rr["string"][8] * 2 + rr["string"][9] * 1
            if minute > 59:
                continue
            minute = str(minute) if minute >= 10 else "0" + str(minute)
            record.append(str(hour) + ":" + minute)
        return record


so = Solution()

print(set(so.readBinaryWatch(0)) == set(["0:00"]))
print(set(so.readBinaryWatch(1)) == set(["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]))

