'''
1033. 移动石子直到连续
三枚石子放置在数轴上，位置分别为 a，b，c。
每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，
并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。
当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]
示例 1：
输入：a = 1, b = 2, c = 5
输出：[1, 2]
解释：将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。
示例 2：
输入：a = 4, b = 3, c = 2
输出：[0, 0]
解释：我们无法进行任何移动。
提示：
1 <= a <= 100
1 <= b <= 100
1 <= c <= 100
a != b, b != c, c != a
'''

from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:  # 贪心的思路
        # 获取最小的移动
        record = [a, b, c]
        record.sort()
        if record[1] - record[0] == 1 and record[2] - record[1] == 1:
            min_m = 0
            max_m = 0
        elif record[1] - record[0] != 1 and record[2] - record[1] != 1:
            if record[1] - record[0] == 2 or record[2] - record[1] == 2:
                min_m = 1
            else:
                min_m = 2
            max_m = record[2] - record[0] - 2
        else:
            min_m = 1
            max_m = record[2] - record[0] - 2
        # 获取最大的移动

        return [min_m, max_m]


so = Solution()

print(so.numMovesStones(1, 2, 5) == [1, 2])
print(so.numMovesStones(4, 3, 2) == [0, 0])
print(so.numMovesStones(3, 5, 1) == [1, 2])
