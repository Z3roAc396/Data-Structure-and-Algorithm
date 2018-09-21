class SingleLinkedList:

    class Node:

        def __init__(self, data):
            self.data=data
            self.next=None

    def __init__(self):
        self.head=None


class DoubleLinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev=None

    def __init__(self):
        self.head = None

    def search(self, element):
        x=self.head

        while x.data!=element and x!=None:
            x=x.next
        return x
    def insert(self, node):
        x.next=self.head
        if self.head!=None:
            self.head.prev=x.next
        self.head=x
        x.prev=None

    def delete(self,node):
        if node.prev!=None:
            node.prev.next=node.next
        else:
            self.head=node.next
        if node.next!=None:
            node.next.prev=node.prev

    