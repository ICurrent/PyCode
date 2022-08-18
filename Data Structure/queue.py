from data_struc import Stack

class Queue(Stack):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()