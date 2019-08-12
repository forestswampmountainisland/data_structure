import DoublePointNode

class CirculatList:
    def __init__(self):
        self.head = DoublePointNode.Node(None)
        self.tail = DoublePointNode.Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.length = 0

    def get(self, i):
        
