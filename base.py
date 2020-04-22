# 定义一版的数据结构


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def create_tree(node_list):
        root = None
        nodes = []
        for index, node in enumerate(node_list):
            if node is not None:
                nodes.append(TreeNode(node))
                root = nodes[0]
            else:
                nodes.append(node)
        before_index = 0  # 上一层次的起始index
        index = start_index_c = 1  # 当前的index起始
        before_count = 1  # 上一层次非空节点
        current_count = 0  # 当前有效节点数
        left_tag = True
        while index < len(nodes):
            if nodes[before_index]:
                if nodes[index]:
                    current_count += 1
                if left_tag:
                    nodes[before_index].left = nodes[index]
                    index += 1
                    left_tag = False
                else:
                    nodes[before_index].right = nodes[index]
                    left_tag = True
                    index += 1
                    if index == before_count * 2 + start_index_c:
                        before_count = current_count
                        current_count = 0
                        before_index = start_index_c
                        start_index_c = index
                    else:
                        before_index += 1
            else:
                before_index += 1
        return root