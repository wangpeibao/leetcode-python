'''
739. 每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
'''

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        sort_result = []
        length = len(T)
        result = [0] * length
        index = 0
        while index < length:
            if sort_result:
                if T[index] > sort_result[-1][1]:
                    result[sort_result[-1][0]] = index - sort_result[-1][0]
                    sort_result.pop(-1)
                else:
                    sort_result.append((index, T[index]))
                    index += 1
            else:
                sort_result.append((index, T[index]))
                index += 1
        return result


so = Solution()

print(so.dailyTemperatures())