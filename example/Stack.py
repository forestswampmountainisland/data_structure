class Stack:
    def __init__(self):
        self.stacks = []

    def push(self, data):
        self.stacks.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stacks.pop()

    def isEmpty(self):
        return len(self.stacks) == 0

