'''
687. 最长同值路径
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:
2
示例 2:
输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:
2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
'''
from base import TreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_length = 0

        def _find_next(p):
            if not p:
                return None, 0
            left_val, left_length = _find_next(p.left)
            right_val, right_length = _find_next(p.right)
            if p.val == left_val and p.val == right_val:
                if left_length + right_length + 2 > self.max_length:
                    self.max_length = left_length + right_length + 2
                return p.val, max(left_length, right_length) + 1
            elif p.val == left_val:
                if left_length + 1 > self.max_length:
                    self.max_length = left_length + 1
                return p.val, left_length + 1
            elif p.val == right_val:
                if right_length + 1 > self.max_length:
                    self.max_length = right_length + 1
                return p.val, right_length + 1
            else:
                return p.val, 0

        _find_next(root)
        return self.max_length




so = Solution()

print(so.longestUnivaluePath(TreeNode.create_tree([5, 4, 5, 1, 1, None, 5])) == 2)
print(so.longestUnivaluePath(TreeNode.create_tree([1, 4, 5, 4, 4, None, 5])) == 2)