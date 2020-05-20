'''
669. 修剪二叉搜索树
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
'''
from base import TreeNode


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def _find_next(p):
            if not p:
                return
            if p.val >= L and p.val <= R:
                p.left = _find_next(p.left)
                p.right = _find_next(p.right)
                return p
            elif p.val < L:
                return _find_next(p.right)
            else:
                return _find_next(p.left)

        root = _find_next(root)
        return root

so = Solution()

# print(so.trimBST(TreeNode.create_tree([1, 0, 2]), 1, 2))
print(so.trimBST(TreeNode.create_tree([3, 0, 4, None, 2, None, None, 1]), 1, 3))
