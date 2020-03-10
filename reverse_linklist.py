class Node(object):
    def __init__(self, item):
        self.item = item 
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head==None

    def append(self, item):
        if self.is_empty(): self.head = Node(item); return 
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(item)

    def tarvel(self):
        if self.is_empty(): print("Empty"); return
        cur = self.head
        while cur: 
            print(cur.item, end=" ")
            cur = cur.next
        print( )

    def reverse(self):
        if self.is_empty(): print("Empty"); return 
        temp, i = [], 1
        cur = self.head
        while cur:
            temp.append(cur.item)
            cur = cur.next
        cur = self.head
        while cur:
            cur.item = temp[-i]
            cur = cur.next
            i += 1

    def reverse_(self):
        if self.is_empty(): print("Empty"); return 
        pre = None
        cur = self.head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        self.head = pre

if __name__ == "__main__":
    L = LinkList()
    for i in range(2, 8):
        L.append(i)
    L.tarvel()
    L.reverse()
    L.tarvel()
    L.reverse_()
    L.tarvel()