'''
849. 到最近的人的最大距离
在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
至少有一个空座位，且至少有一人坐在座位上。
亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
返回他到离他最近的人的最大距离。
示例 1：
输入：[1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。
示例 2：
输入：[1,0,0,0]
输出：3
解释：
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。
提示：
2 <= seats.length <= 20000
seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。
'''

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:  # 遍历获取所有有人的index,注意两头的处理
        max_val = 0
        before_index = None
        length = len(seats)
        for index, val in enumerate(seats):
            if val == 1:
                if before_index is None:
                    max_val = index
                else:
                    if (index - before_index) // 2 > max_val:
                        max_val = (index - before_index) // 2
                before_index = index
            else:
                if index == length - 1:
                    if index - before_index > max_val:
                        max_val = index - before_index
        return max_val



so = Solution()

print(so.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2)
print(so.maxDistToClosest([1, 0, 0, 0]) == 3)
