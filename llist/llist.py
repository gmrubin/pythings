class llist:
    def __init__(self):
        self.length = 0
        self.head = None

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

def printList(node):
    lst = []
    while node:
        lst.append(node.__str__())
        node = node.next
    print lst

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
