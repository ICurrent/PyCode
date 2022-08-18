## Data Structure
# Built-In: # List # Set # Tuple # String # Integer # Dictionary
# User-defined: # Stack # Queue # Heap # Matrix # Binary Tree # Balanced Tree # Rebalanced Tree # Array # Graph

class Stack:
    MAX_ELEMENT = 5

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        if len(self.items) < Stack.MAX_ELEMENT:
            self.items.append(item)
        else:
            raise RuntimeError("List is full")
        #or
        # if self.size() == Stack.MAX_SIZE:
        #     raise RuntimeError('Stack is full')
        # self.items.append(item)

    def peek(self):
        if self.is_empty():
            raise RecursionError ("LLst is empty")
        return self.items[0]

    def pop(self):
        if  self.is_empty():
            raise RuntimeError ("List is empty")
        return self.items.pop()
        
    def display(self):
        return self.items


class Queue(Stack):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    stk = Stack()
    que = Queue()

    entry = input("Enter the data structure type: ")
    data_structure = ''
    if entry.lower() == 'stack':
        data_structure = stk 
    elif entry.lower() == 'queue':
        data_structure = que 
    else:
        pass

    while True:
        print("1.Push") 
        print("2.Pop") 
        print("3.Peek") 
        print("4.Size")
        print("5.Display") 
        print("6.Quit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            x = int(input("Enter an element to pushed: "))
            data_structure.push(x)
        elif choice == 2:
            x = data_structure.pop()
            print(f"Element {x} was popped out")
        elif choice == 3:
            print(f"Element {data_structure.peek()} is the first elment")
        elif choice == 4:
            print("Size of stack " , data_structure.size()) 
        elif choice == 5:
            print(data_structure.display())      
        elif choice == 6:
          break
        else:
          print("Wrong choice") 
        print() 