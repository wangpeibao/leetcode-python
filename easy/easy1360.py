"""
1360. 日期之间隔几天
请你编写一个程序来计算两个日期之间隔了多少天。
日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。
示例 1：
输入：date1 = "2019-06-29", date2 = "2019-06-30"
输出：1
示例 2：
输入：date1 = "2020-01-15", date2 = "2019-12-31"
输出：15
提示：
给定的日期是 1971 年到 2100 年之间的有效日期。
"""


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        stand31 = [1, 3, 5, 7, 8, 10, 12]

        def _get_month(year, m):
            count = 0
            for mm in range(1, m):
                if mm in stand31:
                    count += 31
                elif mm == 2:
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        count += 29
                    else:
                        count += 28
                else:
                    count += 30
            return count

        def _get_year(y1, y2):
            count = 0
            for y in range(y1, y2):
                if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                    count += 366
                else:
                    count += 365
            return count

        # 解题思路，组合成年份月份的数组
        year1 = int(date1[:4])
        year2 = int(date2[:4])

        d1 = int(date1[8:]) - 1  # 转化成1号
        d2 = int(date2[8:]) - 1  # 转化成1号

        month1 = _get_month(year1, int(date1[5:7]))
        month2 = _get_month(year2, int(date2[5:7]))

        if year1 == year2:
            return abs(d1 + month1 - d2 - month2)
        elif year1 > year2:
            y_count = _get_year(year2, year1)
            return y_count + (d1 + month1 - d2 - month2)
        else:
            y_count = _get_year(year1, year2)
            return y_count + (d2 + month2 - d1 - month1)


so = Solution()
# print(so.daysBetweenDates(date1="2019-06-29", date2="2019-06-30") == 1)
# print(so.daysBetweenDates(date1="2020-01-15", date2="2019-12-31") == 15)
print(so.daysBetweenDates("1971-06-29", "2010-09-23") == 14331)
