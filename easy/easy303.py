'''
303. 区域和检索 - 数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

思路：　累加法，用一个数组存储前n项和，这样取中间一段的和就可以用数组末端减去前端的值
'''


class NumArray:

    def __init__(self, nums):  # 累加法
        self.record = [0]
        count = 0
        for num in nums:
            count += num
            self.record.append(count)

    def sumRange(self, i: int, j: int) -> int:
        return self.record[j + 1] - self.record[i]

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2) == 1)
print(obj.sumRange(2, 5) == -1)
print(obj.sumRange(0, 5) == -3)