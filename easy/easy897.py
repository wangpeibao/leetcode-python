'''
897. 递增顺序查找树
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
示例 ：
输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9

提示：
给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。
'''
from base import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def _find_mid(p):
            if not p.left:
                if not p.right:
                    return p, p
                r1, r2 = _find_mid(p.right)
                p.right = r1
                return p, r2
            l1, l2 = _find_mid(p.left)
            l2.right = p
            p.left = None
            if not p.right:
                return l1, p
            r1, r2 = _find_mid(p.right)
            p.right = r1
            return l1, r2
        root1, root2 = _find_mid(root)
        return root1

so = Solution()

print(so.increasingBST(TreeNode.create_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])))
