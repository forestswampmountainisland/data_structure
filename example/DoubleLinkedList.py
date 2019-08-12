import DoublePointNode

class DoubleLinkedList:
    def __init__(self):
        # 也可以再多维护一个末尾节点，这样可以提高效率
        # 比如说append就变成了O(1)的操作
        # get也可以根据i的大小决定从尾还是头遍历
        self.head = DoublePointNode.Node(None)
        self.length = 0

    def append(self, data):
        self.insert(data, self.length)

    def insert(self, data, i):
        previous = self.get(i - 1)
        try:
            next = self.get(i + 1)
        except IndexError:
            next = None
        current = DoublePointNode.Node(data)
        previous.next = current
        current.prev = previous
        if next is not None:
            next.prev = current
            current.next = next
        self.length += 1

    def remove(self, i):
        previous = self.get(i - 1)
        try:
            next = self.get(i + 1)
        except IndexError:
            next = None
        current = previous.next
        previous.next = next
        if next is not None:
            next.prev = previous
        return current

    def get(self, i):
        if i < 0:
            raise IndexError("Out of index")
        current = self.head
        while i >= 0:
            current = current.next
            if current is None:
                raise IndexError("Out of index")
            i -= 1
        return current

    class Iterator:
        def __init__(self, list):
            self.list = list
            self.current = self.list.head

        def __next__(self):
            self.current = self.current.next
            if self.current is None:
                raise StopIteration()
            return self.current

    def __iter__(self):
        return DoubleLinkedList.Iterator(self)
