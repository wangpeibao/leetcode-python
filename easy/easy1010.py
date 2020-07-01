'''
1010. 总持续时间可被 60 整除的歌曲
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。
示例 1：
输入：[30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整数：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
示例 2：
输入：[60,60,60]
输出：3
解释：所有三对的总持续时间都是 120，可以被 60 整数。
提示：
1 <= time.length <= 60000
1 <= time[i] <= 500
'''

from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:  # 暴力破解法(超出时间限制)，改用hash法
        has_dict = dict()
        for i in range(60):
            has_dict[i] = []
        for index, t in enumerate(time):
            has_dict[t % 60].append(index)
        count = 0
        for i in range(60):
            if i == 0 or i == 30:
                count += len(has_dict[i]) * (len(has_dict[i]) - 1) // 2
            else:
                length = len(has_dict[60 - i])
                j = 0
                for index in has_dict[i]:
                    while j < length:
                        if has_dict[60 - i][j] < index:
                            j += 1
                        else:
                            count += length - j
                            break
        return count


so = Solution()

print(so.numPairsDivisibleBy60([30, 20, 150, 100, 40]) == 3)
print(so.numPairsDivisibleBy60([60, 60, 60]) == 3)
