'''
872. 叶子相似的树
请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

提示：
给定的两颗树可能会有 1 到 200 个结点。
给定的两颗树上的值介于 0 到 200 之间。
'''

from base import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        result1 = []
        result2 = []

        def _get_leaf1(root):
            if not root:
                return
            if not root.left and not root.right:
                result1.append(root.val)
            else:
                if root.left:
                    _get_leaf1(root.left)
                if root.right:
                    _get_leaf1(root.right)

        def _get_leaf2(root):
            if not root:
                return
            if not root.left and not root.right:
                result2.append(root.val)
            else:
                if root.left:
                    _get_leaf2(root.left)
                if root.right:
                    _get_leaf2(root.right)

        _get_leaf1(root1)
        _get_leaf2(root2)
        return result1 == result2




