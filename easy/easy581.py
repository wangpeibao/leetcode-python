'''
581. 最短无序连续子数组
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。
示例 1:
输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :
输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
'''

class Solution:
    def findUnsortedSubarray(self, nums) -> int:  # 排序之后删除两端相同的
        before_nums = nums.copy()
        nums.sort()
        count = 0
        index = 0
        while index < len(nums) and before_nums[index] == nums[index]:
            count += 1
            index += 1
        if count == len(nums):
            return 0
        else:
            index = len(nums) - 1
            while index >= 0 and before_nums[index] == nums[index]:
                count += 1
                index -= 1
            return len(nums) - count




    def findUnsortedSubarray1(self, nums) -> int:  # 形如选择排序
        before = 0
        for index, value in enumerate(nums):
            status = True
            for stand in nums[index + 1:]:
                if value > stand:
                    status = False
                    break
            if status:
                before += 1
            else:
                break
        after = 0
        nums_after = nums[before:]
        nums_after.reverse()
        for index, value in enumerate(nums_after):
            status = True
            for stand in nums_after[index + 1:]:
                if value < stand:
                    status = False
                    break
            if status:
                after += 1
            else:
                break
        return len(nums) - before - after

so = Solution()

print(so.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5)
print(so.findUnsortedSubarray([1, 2, 3, 4]) == 0)
