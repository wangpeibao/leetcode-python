'''
面试题 16.18. 模式匹配
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。
例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），
该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。
示例 1：
输入： pattern = "abba", value = "dogcatcatdog"
输出： true
示例 2：
输入： pattern = "abba", value = "dogcatcatfish"
输出： false
示例 3：
输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false
示例 4：
输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则
提示：
0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
'''


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:  # 暴力枚举法
        count_ab = [0, 0]
        for p in pattern:
            if p == "a":
                count_ab[0] += 1
            else:
                count_ab[1] += 1
        length = len(value)
        if count_ab[0] == 0 and count_ab[1] == 0:
            if length == 0:
                return True
            else:
                return False
        elif count_ab[0] != 0 and count_ab[1] != 0:
            for lena in range(length + 1):
                if lena * count_ab[0] <= length:
                    other_length = length - lena * count_ab[0]
                    if other_length % count_ab[1] == 0:
                        lenb = other_length // count_ab[1]
                        # 求出ab分别代表的长度，开始验证
                        start = 0
                        standa = ""
                        standb = ""
                        status = True
                        for pa in pattern:
                            if pa == "a":
                                if not standa:
                                    standa = value[start: start + lena]
                                else:
                                    if standa != value[start: start + lena]:
                                        status = False
                                        break
                                start += lena
                            else:  # pa == "b":
                                if not standb:
                                    standb = value[start: start + lenb]
                                else:
                                    if standb != value[start: start + lenb]:
                                        status = False
                                        break
                                start += lenb
                        if status and standa != standb:
                            return True
            return False
        else:
            count = sum(count_ab)
            if length % count != 0:
                return False
            self_length = length // count
            str_stand = value[:self_length]
            for i in range(count):
                if value[i*self_length: (i + 1)*self_length] != str_stand:
                    return False
            return True





so = Solution()


print(so.patternMatching("abba", "dogcatcatdog") == True)
print(so.patternMatching("abba", "dogcatcatfish") == False)
print(so.patternMatching("aaaa", "dogcatcatdog") == False)
print(so.patternMatching("abba", "dogdogdogdog") == True)
print(so.patternMatching("ab", "") == False)
