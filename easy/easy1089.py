'''
1089. 复写零
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
注意：请不要在超过该数组长度的位置写入元素。
要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
示例 1：
输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
示例 2：
输入：[1,2,3]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]
提示：
1 <= arr.length <= 10000
0 <= arr[i] <= 9
'''

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 获取每个元素之前有多少个零
        stand = []
        zero_count = 0
        for index, a in enumerate(arr):
            stand.append(zero_count)
            if a == 0:
                zero_count += 1
        length = len(stand)
        index = length - 1
        while index >= 0:
            if stand[index] + index < length:
                if stand[index] != 0:
                    arr[stand[index] + index] = arr[index]
                    arr[index] = 0
            else:
                arr[index] = 0
            index -= 1

so = Solution()
a = [1, 0, 2, 3, 0, 4, 5, 0]
so.duplicateZeros(a)
print(a == [1, 0, 0, 2, 3, 0, 0, 4])
b = [1, 2, 3]
so.duplicateZeros(b)
print(b == [1, 2, 3])
