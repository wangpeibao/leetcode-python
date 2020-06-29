'''
993. 二叉树的堂兄弟节点
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
示例 1：
输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：
输入：root = [1,2,3,None,4,None,5], x = 5, y = 4
输出：true
示例 3：
输入：root = [1,2,3,None,4], x = 2, y = 3
输出：false
提示：
二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。
'''
from base import TreeNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        has_dict = dict()
        before = [root]
        deep = 1
        while before:
            after = []
            for bb in before:
                if bb:
                    if bb.left:
                        after.append(bb.left)
                        has_dict[bb.left.val] = (bb.val, deep)
                    if bb.right:
                        after.append(bb.right)
                        has_dict[bb.right.val] = (bb.val, deep)
            before = after
            deep += 1
        if x in has_dict.keys() and y in has_dict.keys():
            if has_dict[x][0] != has_dict[y][0] and has_dict[x][1] == has_dict[y][1]:
                return True
        return False


so = Solution()

print(so.isCousins(TreeNode.create_tree([1, 2, 3, 4]), 4, 3) == False)
print(so.isCousins(TreeNode.create_tree([1, 2, 3, None, 4, None, 5]), 5, 4) == True)
print(so.isCousins(TreeNode.create_tree([1, 2, 3, None, 4]), 2, 3) == False)