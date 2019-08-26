class BinarySearchTreeNode:
    def __init__(self, data):
        self.root = None
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def append(self, data):
        if self.root is None:
            self.root = BinarySearchTreeNode(data)
            return
        current = self.root
        while current is not None:
            if current.data == data:
                raise AttributeError("data value should be unique")
            elif current.data < data:
                if current.right is None:
                    current.right = BinarySearchTreeNode(data)
                    return
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = BinarySearchTreeNode(data)
                    return
                else:
                    current = current.left

    def find(self, data):
        currentRoot = self.root
        while currentRoot is not None:
            if currentRoot.data == data:
                return currentRoot
            elif currentRoot.data < data:
                currentRoot = currentRoot.right
            else:
                currentRoot = currentRoot.left
        else:
            return None