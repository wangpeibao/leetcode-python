'''
453. 最小移动次数使数组元素相等
给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。

示例:
输入:
[1,2,3]
输出:
3
解释:
只需要3次移动（注意每次移动会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''


class Solution:
    def minMoves1(self, nums) -> int:  # 暴力破解法
        count = 0
        status = True
        while status:
            status = False
            max_index = 0
            max_value = None
            for index, n in enumerate(nums):
                if index == 0:
                    max_value = n
                    max_index = index
                else:
                    if n > max_value:
                        max_value = n
                        nums[max_index] += 1
                        status = True
                    else:
                        if n < max_value:
                            status = True
                        nums[index] += 1
            if status:
                count += 1
        return count

    def minMoves(self, nums) -> int:  # 除最值外加1，相当于最大值-1
        # 计算最小值
        min_value = min(nums)
        count = 0
        for n in nums:
            count += n - min_value
        return count


so = Solution()

print(so.minMoves([1, 2, 3]) == 3)
print(so.minMoves([1, 2, 3, 4]) == 6)
