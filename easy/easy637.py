'''
637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode):
        # 层级遍历
        result = []
        before = [root]
        while before:
            after = []
            self_count = 0
            for bb in before:
                self_count += bb.val
                if bb.left:
                    after.append(bb.left)
                if bb.right:
                    after.append(bb.right)
            result.append(self_count / len(before))
            before = after
        return result

so = Solution()
