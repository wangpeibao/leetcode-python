'''
414. 第三大的数
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:
输入: [3, 2, 1]
输出: 1
解释: 第三大的数是 1.
示例 2:
输入: [1, 2]
输出: 2
解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:
输入: [2, 2, 3, 1]
输出: 1
解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

思路：按照找最大值的方式，找三次
'''


class Solution:
    def thirdMax(self, nums) -> int:
        m_value = None
        for n in nums:
            if m_value is None:
                m_value = n
            else:
                if n > m_value:
                    m_value = n
        s_value = None
        for n in nums:
            if n < m_value:
                if s_value is None:
                    s_value = n
                else:
                    if n > s_value:
                        s_value = n
        if s_value is None:
            return m_value
        t_value = None
        for n in nums:
            if n < s_value:
                if t_value is None:
                    t_value = n
                else:
                    if n > t_value:
                        t_value = n
        if t_value is None:
            return m_value
        return t_value

so = Solution()

print(so.thirdMax([3, 2, 1]) == 1)
print(so.thirdMax([1, 2]) == 2)
print(so.thirdMax([2, 2, 3, 1]) == 1)