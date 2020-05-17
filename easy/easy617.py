'''
617. 合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。
示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
'''
from base import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def _find_first(p1, p2):
            p1.val += p2.val
            if p1.left and p2.left:
                _find_first(p1.left, p2.left)
            elif not p1.left and p2.left:
                p1.left = p2.left
            if p1.right and p2.right:
                _find_first(p1.right, p2.right)
            elif not p1.right and p2.right:
                p1.right = p2.right

        if not t1 and not t2:
            return t1
        elif t1 and t2:
            _find_first(t1, t2)
            return t1
        else:
            return t1 if t1 else t2

so = Solution()

so.mergeTrees(TreeNode.create_tree())