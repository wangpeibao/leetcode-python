'''
404. 左叶子之和
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

思路：中序遍历，找到所有的左叶子节点，求和
'''
from base import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = []
        def _find_left(p):
            if not p:
                return
            else:
                if p.left:
                    if not p.left.left and not p.left.right:
                        result.append(p.left.val)
                _find_left(p.left)
                _find_left(p.right)
        _find_left(root)
        return sum(result)

so = Solution()

print(so.sumOfLeftLeaves(TreeNode.create_tree([3, 9, 20, None, None, 15, 7])) == 24)
