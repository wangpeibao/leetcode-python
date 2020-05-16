'''
5396. 连续字符  显示英文描述
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
请你返回字符串的能量
'''

class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_count = 1
        before = None
        for index, ss in enumerate(s):
            if ss == before:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                before = ss
                count = 1
        return max_count

so = Solution()

print(so.maxPower("tourist") == 1)
print(so.maxPower("hooraaaaaaaaaaay") == 11)
print(so.maxPower("triplepillooooow") == 5)
print(so.maxPower("abbcccddddeeeeedcba") == 5)