from inspect import stack


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


if __name__ == '__main__':
    stk = stack()

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
            stk.push(x)
        elif choice == 2:
            x = stk.pop()
            print(f"Element {x} was popped out")
        elif choice == 3:
            print(f"Element {stk.peek()} is the first elment")
        elif choice == 4:
            print("Size of stack " , stk.size()) 
        elif choice == 5:
            print(stk.display())      
        elif choice == 6:
          break
        else:
          print("Wrong choice") 
        print() 