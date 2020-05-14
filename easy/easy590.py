'''
590. N叉树的后序遍历
给定一个 N 叉树，返回其节点值的后序遍历。
例如，给定一个 3叉树 :
返回其后序遍历: [5,6,3,2,4,1].
说明: 递归法很简单，你可以使用迭代法完成此题吗?
'''


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node'):
        result = []

        def _root_last(p):
            if not p:
                return
            else:
                for child in p.children:
                    _root_last(child)
                result.append(p.val)

        _root_last(root)
        return result