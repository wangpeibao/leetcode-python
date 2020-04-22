'''
199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

思路：　适用层次遍历，取每次遍历的最后一个节点即可
'''
from base import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        result = [[root]]
        while True:
            after = []
            for rr in result[-1]:
                if rr.left:
                    after.append(rr.left)
                if rr.right:
                    after.append(rr.right)
            if not after:
                break
            else:
                result.append(after)
        return [r[-1].val for r in result]



so = Solution()

examples = [
    {"root": [1, 2, 3, None, 5, None, 4], "result": [1, 3, 4]}
]

for exa in examples:
    result = so.rightSideView(TreeNode.create_tree(exa["root"]))
    print(result == exa["result"])
