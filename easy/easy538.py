'''
538. 把二叉搜索树转换为累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
'''
from base import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:  # 根据特性，先右节点
        def _get_count(p):
            if not p:
                return 0
            count = p.val
            count += _get_count(p.left)
            count += _get_count(p.right)
            return count

        def _get_result(p, before):
            p.val += _get_count(p.right) + before
            _get_count(p.right)





so = Solution()

print(so.convertBST(TreeNode.create_tree([5, 2, 13])))
print(so.convertBST(TreeNode.create_tree([2, 0, 3, -4, 1])))