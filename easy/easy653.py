'''
653. 两数之和 IV - 输入 BST
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
案例 1:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
案例 2:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
输出: False
'''
from base import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:  # 将搜索树整理成数组
        record = []
        def _get_list(p):
            if not p:
                return
            _get_list(p.left)
            record.append(p.val)
            _get_list(p.right)

        _get_list(root)
        # 使用双指针法
        start = 0
        end = len(record) - 1
        while start < end:
            if record[start] + record[end] == k:
                return True
            elif record[start] + record[end] > k:
                end -= 1
            else:
                start += 1
        return False

so = Solution()


print(so.findTarget(TreeNode.create_tree([5, 3, 6, 2, 4, None, 7]), 9) == True)
print(so.findTarget(TreeNode.create_tree([5, 3, 6, 2, 4, None, 7]), 28) == False)