'''
530. 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：

输入：

   1
    \
     3
    /
   2

输出：
1
解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
提示：
树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:  # 根据搜索数据的特性，比较一个节点与其子节点的差最小，左子树的最右，右子树的最左
        min_val = None
        # 层次遍历
        before = [root]
        while before:
            after = []
            for b in before:
                # 获取当前的左子树最大和右子树最小
                if b.left:
                    bleft = b.left
                    while bleft.right:
                        bleft = bleft.right
                    min_val = abs(b.val - bleft.val) if min_val is None else min(min_val, abs(b.val - bleft.val))
                if b.right:
                    bright = b.right
                    while bright.left:
                        bright = bright.left
                    min_val = abs(b.val - bright.val) if min_val is None else min(min_val, abs(b.val - bright.val))
                if b.left:
                    after.append(b.left)
                if b.right:
                    after.append(b.right)
            before = after
        return min_val

so = Solution()

print(so.getMinimumDifference(TreeNode.create_tree([1, None, 3, 2])) == 1)