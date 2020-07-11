# 思路
# 只有BFS（广度遍历）从用queen，前序遍历（深度遍历），中序遍历都用stack；
# 中序遍历比较特殊，需要进一步理解，后序遍历可以根据前序遍历做输出更改。

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def append(self, node):
        if not self.root:
            self.root = node
            return 
        node_list = [self.root]
        while node_list:
            cur_node = node_list.pop(0)
            if not cur_node.left:
                cur_node.left = node
                return 
            if not cur_node.right:
                cur_node.right = node
                return 
            node_list.append(cur_node.left)
            node_list.append(cur_node.right)

    def foreward_travel(self):
        if not self.root: return 
        node_list = [self.root]
        while node_list:
            cur_node = node_list.pop()
            if not cur_node: continue
            print(cur_node.val, end=' ')
            node_list.append(cur_node.right)
            node_list.append(cur_node.left)
        print(" ")

    def mid_travel(self):
        if not self.root: return 
        node_list, cur_node = [], self.root
        while node_list or cur_node:
            while cur_node:
                node_list.append(cur_node)
                cur_node = cur_node.left
            cur_node = node_list.pop()
            print(cur_node.val, end=" ")
            cur_node = cur_node.right
        print(" ")

    def backward_travel(self):
        pass 

if __name__ == "__main__":
    binary_tree = BinaryTree()
    for i in [4, 2, 5, 1, 3]:
        node = Node(i)
        binary_tree.append(node)
    binary_tree.foreward_travel()
    binary_tree.mid_travel()