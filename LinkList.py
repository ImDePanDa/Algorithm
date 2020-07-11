class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    def append(self, node):
        if not self.head: 
            self.head = node 
            return 
        cur_node = self.head
        while cur_node.next: 
            cur_node = cur_node.next
        cur_node.next = node

    def travel(self):
        if not self.head: return 
        cur_node = self.head 
        while cur_node.next:
            print(cur_node.val, end=' ')
            cur_node = cur_node.next
        print(cur_node.val)

if __name__ == "__main__":
    linklist = LinkList()
    for i in range(2, 12):
        node = Node(i)
        linklist.append(node)
    linklist.travel()