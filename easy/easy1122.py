'''
1122. 数组的相对排序
给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
提示：
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中
'''

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        set2 = set(arr2)
        has_dict = dict()
        other_record = []
        for a1 in arr1:
            if a1 in set2:
                if a1 in has_dict.keys():
                    has_dict[a1] += 1
                else:
                    has_dict[a1] = 1
            else:
                other_record.append(a1)
        record = []
        for a2 in arr2:
            if a2 in has_dict.keys():
                record += [a2] * has_dict[a2]
        other_record.sort()
        return record + other_record


so = Solution()

print(so.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19])
