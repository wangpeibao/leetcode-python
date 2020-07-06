'''
1022. 从根到叶的二进制数之和
给出一棵二叉树，其上每个结点的值都是 0 或 1 。
每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
以 10^9 + 7 为模，返回这些数字之和。
示例：
输入：[1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
提示：
树中的结点数介于 1 和 1000 之间。
node.val 为 0 或 1 。
'''
from base import TreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # 层次遍历 求和
        before = [[root, root.val]]
        count = 0
        stand = 10 ** 9 + 7
        while before:
            after = []
            for bb, val in before:
                if not bb.left and not bb.right:
                    count = (count + val) % stand
                else:
                    if bb.left:
                        after.append([bb.left, val * 2 + bb.left.val])
                    if bb.right:
                        after.append([bb.right, val * 2 + bb.right.val])
            before = after
        return count


so = Solution()

print(so.sumRootToLeaf(TreeNode.create_tree([1,0,1,0,1,0,1])) == 22)