'''
437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
'''
from base import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:  # 先序遍历
        result = []

        def _find_first(p, before):
            if not p:
                return
            else:
                after = [p.val]
                if p.val == sum:
                    result.append(1)
                for bb in before:
                    after.append(bb + p.val)
                    if bb + p.val == sum:
                        result.append(1)
                _find_first(p.left, after)
                _find_first(p.right, after)
        _find_first(root, [])

        return len(result)


so = Solution()

print(so.pathSum(TreeNode.create_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8) == 3)

