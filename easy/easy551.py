'''
551. 学生出勤记录 I
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
你需要根据这个学生的出勤记录判断他是否会被奖赏。
示例 1:
输入: "PPALLP"
输出: True
示例 2:
输入: "PPALLL"
输出: False
'''


class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0
        for val in s:
            if val == "A":
                a_count += 1
                if a_count == 2:
                    return False
                l_count = 0
            elif val == "L":
                if l_count:
                    l_count += 1
                    if l_count == 3:
                        return False
                else:
                    l_count += 1
            else:
                l_count = 0
        return True

so = Solution()

print(so.checkRecord("PPALLP") == True)
print(so.checkRecord("PPALLL") == False)