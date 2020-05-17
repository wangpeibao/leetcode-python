'''
5414. 收藏清单  显示英文描述
给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。
请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。
'''


class Solution:
    def peopleIndexes(self, favoriteCompanies):  # hash法
        hash_list = []
        for fa in favoriteCompanies:
            hash_list.append(set(fa))
        result = []
        for index, val in enumerate(hash_list):
            status = True
            for stand in hash_list[:index] + hash_list[index + 1:]:
                if val.issubset(stand):
                    status = False
                    break
            if status:
                result.append(index)
        return result



so = Solution()

print(so.peopleIndexes([["leetcode"], ["google"], ["facebook"], ["amazon"]]) == [0, 1, 2, 3])
print(so.peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]) == [0, 1])
print(so.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]) == [0, 1, 4])

