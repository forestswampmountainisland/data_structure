class BinaryNode:
    def __init__(self, data):
        self.data = data

class BinaryTree:
    def __init__(self, data):
        self.root = BinaryNode(data)
        self.left = None
        self.right = None

    def appendChild(self, tree, isLeft = True):
        if isLeft:
            self.left = tree
        else:
            self.right = tree

    def removeChild(self, isLeft = True):
        if isLeft:
            self.left = None
        else:
            self.right = None

    def preOrder(self):
        yield self
        if self.left is not None:
            for node in self.left.preOrder():
                yield node
        elif self.right is not None:
            for node in self.right.preOrder():
                yield node
        raise StopIteration()

    def inOrder(self):
        if self.left is not None:
            for node in self.left.preOrder():
                yield node
        yield self
        if self.right is not None:
            for node in self.right.preOrder():
                yield node
        raise StopIteration()

    def postOrder(self):
        if self.left is not None:
            for node in self.left.preOrder():
                yield node
        if self.right is not None:
            for node in self.right.preOrder():
                yield node
        yield self
        raise StopIteration()

    def breadthFirstSearch(self):
        # 用一个队列来存储将要访问的节点
        queue = [self]
        while len(queue) != 0:
            node = queue.pop(0)
            # 将当前节点的左右节点放到队尾，这就保证了左右节点一定在当前节点的兄弟节点之后
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            yield node
        raise StopIteration()

    def depthFirstSearch(self):
        # 用一个栈来存储已经访问过的节点
        if self.left is not None:
            for node in self.left.depthFirstSearch():
                yield node
        if self.right is not None:
            for node in self.right.depthFirstSearch():
                yield node
        yield self
        