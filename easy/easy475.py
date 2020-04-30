'''
475. 供暖器
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
说明:
给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。
示例 1:
输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:
输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
'''


class Solution:
    def findRadius(self, houses, heaters) -> int:  # 思路，将房屋插入到两个相邻取暖器之间，取房屋到两个取暖器之间的最小值，然后这些最小值取最大值
        # 处理取暖器的值
        stand = 2 * 10 ** 9 + 1
        heaters.sort()
        houses.sort()
        heaters = [-stand] + heaters + [stand]
        record = []
        h_index = 0
        for house in houses:
            while heaters[h_index] < house:
                h_index += 1
            record.append(min(house - heaters[h_index - 1], heaters[h_index] - house))
        return max(record)


so = Solution()

# print(so.findRadius([1, 2, 3], [2]) == 1)
# print(so.findRadius([1, 2, 3, 4], [1, 4]) == 1)
# print(so.findRadius([1, 2, 3, 5, 15], [2, 30]) == 13)
print(so.findRadius([474833169, 264817709, 998097157, 817129560],
                    [197493099, 404280278, 893351816, 505795335]) == 104745341)
