import SinglePointNode

# 单链表        
class LinkedList:
    def __init__(self):
        # 我们经常会给链表一个虚假的头指针，因为头节点理论上没有前一个节点，所以假的指针可以保证头节点的操作和其他节点一样
        # 比如删除头节点这个时候就会用这个假的头节点指向第二个节点
        self.head = SinglePointNode.Node(None)
        self.length = 0

    def append(self, data):
        self.insert(data, self.length)
    
    def insert(self, data, i):
        previous = self.get(i - 1)
        # 保存当前插入位置的节点
        current = None if previous.next == None else previous.next
        # 让插入位置前一个的节点的next指针指向插入的节点
        previous.next = SinglePointNode.Node(data)
        # 让插入的节点的next指针指向
        previous.next.next = current
        self.length += 1

    def remove(self, i):
        previous = self.get(i - 1)
        # 保存删除节点的数据来返回
        data = None if previous.next == None else previous.next.data
        # 前一个节点指向删除节点的后一个节点
        previous.next = None if previous.next == None else previous.next.next
        self.length -= 1
        return data

    def update(self, data, i):
        node = self.get(i)
        node.data = data

    def get(self, i):
        current = self.head
        while i >= 0:
            if current == None:
                raise IndexError("Out of index")
            current = current.next
            i -= 1
        return current

    # 用一个内部类将迭代器封装在类内部
    class Iterator:
        def __init__(self, list):
            self.list = list
            self.current = self.list.head
        # 迭代器实现__next__
        def __next__(self):
            self.current = self.current.next
            if self.current == None:
                raise StopIteration()
            return self.current
    
    # LinkedList是一个可迭代对象，返回一个迭代器
    def __iter__(self):
        return self.Iterator(self)
