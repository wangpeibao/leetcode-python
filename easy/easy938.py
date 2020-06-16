'''
938. 二叉搜索树的范围和
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
二叉搜索树保证具有唯一的值。
示例 1：
输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
示例 2：
输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23
提示：
树中的结点数量最多为 10000 个。
最终的答案保证小于 2^31。
'''

from base import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = []
        def _find_root(p):
            if not p:
                return
            if p.val <= R and p.val >= L:
                result.append(p.val)
                _find_root(p.left)
                _find_root(p.right)
            elif p.val < L:
                _find_root(p.right)
            elif p.val > R:
                _find_root(p.left)
        _find_root(root)
        return sum(result)


so = Solution()

print(so.rangeSumBST(TreeNode.create_tree([10,5,15,3,7,None,18]), 7, 15) == 32)
print(so.rangeSumBST(TreeNode.create_tree([10,5,15,3,7,13,18,1,None,6]), 6, 10) == 23)