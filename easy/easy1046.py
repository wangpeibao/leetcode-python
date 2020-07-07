'''
1046. 最后一块石头的重量
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
示例：
输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
提示：
1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        length = len(stones)
        while length > 1:
            if length == 2:
                if stones[0] == stones[1]:
                    return 0
                else:
                    return stones[1] - stones[0]
            else:
                x = stones[length - 2]
                y = stones[length - 1]
                if x == y:
                    if length == 3:
                        return stones[0]
                    else:
                        length -= 2
                else:
                    z = y - x
                    status = False
                    for i in range(length - 2):
                        if z <= stones[i]:
                            stones.insert(i, z)
                            status = True
                            break
                    if not status:
                        stones.insert(length - 2, z)
                    length -= 1
        return stones[0]


so = Solution()

print(so.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1)
