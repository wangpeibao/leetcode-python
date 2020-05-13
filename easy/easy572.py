'''
572. 另一个树的子树
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

'''
from base import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:  # DFS
        def _check(ss, tt):
            if ss and tt:
                if ss.val == tt.val:
                    return _check(ss.left, tt.left) and _check(ss.right, tt.right)
                else:
                    return False
            elif not ss and not tt:
                return True
            else:
                return False

        def _find_next(ss, tt):
            if not ss:
                return False
            return _check(ss, tt) or _find_next(ss.left, tt) or _find_next(ss.right, tt)

        return _find_next(s, t)


so = Solution()

print(so.isSubtree(TreeNode.create_tree([3, 4, 5, 1, 2]), TreeNode.create_tree([4, 1, 2])) == True)
print(so.isSubtree(TreeNode.create_tree([3, 4, 5, 1, 2, None, None, 0]), TreeNode.create_tree([4, 1, 2])) == True)