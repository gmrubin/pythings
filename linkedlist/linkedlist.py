class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def WalkTo(self, index):
        prev = None
        node = self.head
        i = 0

        while (node != None) and (i < index):
            prev = node
            node = node.next
            i += 1
        return node, prev

    def AddNode(self, cargo):
        new_node = Node(cargo)

        if self.head == None:
            self.head = new_node
        elif self.tail != None:
            self.tail.next = new_node

        self.tail = new_node

    def InsertNode(self, cargo, index):
        new_node = Node(cargo)

        node, prev = self.WalkTo(index)

        if prev == None:
            self.head = node

        prev.next = new_node
        new_node.next = node


    def RemoveNode(self, index):

        node, prev = self.WalkTo(index)

        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next

    def PrintList(self):
        node = self.head

        while node != None:
            print node,
            node = node.next

List = LinkedList()
List.AddNode(1)
List.AddNode(2)
List.AddNode(3)
List.AddNode(4)
List.AddNode(5)

List.PrintList()
print
List.RemoveNode(2)
List.PrintList()
print
List.AddNode(2)
List.PrintList()
print
List.InsertNode(17, 1)
List.PrintList()

