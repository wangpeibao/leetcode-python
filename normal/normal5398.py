'''
5398. 统计二叉树中好节点的数目
给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
'''
from base import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def _find_deep(p, max_before):
            if not p:
                return 0
            if p.val >= max_before:
                self.count += 1
                _find_deep(p.left, p.val)
                _find_deep(p.right, p.val)
            else:
                _find_deep(p.left, max_before)
                _find_deep(p.right, max_before)
        _find_deep(root, - 10 ** 4)
        return self.count


so = Solution()

print(so.goodNodes(TreeNode.create_tree([3, 1, 4, 3, None, 1, 5])) == 4)
print(so.goodNodes(TreeNode.create_tree([3, 3, None, 4, 2])) == 3)
print(so.goodNodes(TreeNode.create_tree([1])) == 1)
