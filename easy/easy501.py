'''
501. 二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
假定 BST 有如下定义：
结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].
提示：如果众数超过1个，不需考虑输出顺序
进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import TreeNode


class Solution:
    def findMode(self, root: TreeNode):  # 递归处理，左右和根节点数统计和
        val_dict = dict()
        def _find_next(p):
            if not p:
                return
            if p.val in val_dict.keys():
                val_dict[p.val] += 1
            else:
                val_dict[p.val] = 1
            _find_next(p.left)
            _find_next(p.right)
        _find_next(root)
        # 获取字典最大值
        result = []
        max_value = 0
        for key, val in val_dict.items():
            if val > max_value:
                max_value = val
                result = [key]
            elif val == max_value:
                result.append(key)
            else:
                pass
        return result

so = Solution()

print(so.findMode(TreeNode.create_tree([1, None, 2, 2])) == [2])
print(so.findMode(TreeNode.create_tree([1, None, 2])) == [1, 2])
