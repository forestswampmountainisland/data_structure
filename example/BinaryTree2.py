import BinaryTreeNode

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def setRoot(self, data):
        if self.root is not None:
            self.root.data = data
        else:
            self.root = BinaryTreeNode.Node(data)

    def addChild(self, node, data, isLeft = True):
        if isLeft:
            node.left = BinaryTreeNode.Node(data)
        else:
            node.right = BinaryTreeNode.Node(data)