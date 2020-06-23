'''
965. 单值二叉树
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。
示例 1：
输入：[1,1,1,1,1,null,1]
输出：true
示例 2：
输入：[2,2,2,5,2]
输出：false
提示：
给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99] 。
'''
from base import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def _find_next(p):
            if not p:
                return True, None
            ls, lv = _find_next(p.left)
            rs, rv = _find_next(p.right)
            if ls and rs:
                if (lv is None or lv == p.val) and (rv is None or rv == p.val):
                    return True, p.val
            return False, None

        status, val = _find_next(root)
        return status


so = Solution()

print(so.isUnivalTree(TreeNode.create_tree([1, 1, 1, 1, 1, None, 1])) == True)
print(so.isUnivalTree(TreeNode.create_tree([2, 2, 2, 5, 2])) == False)

