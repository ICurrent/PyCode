class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def setItem(self, item):
        self.item = item

    def getItem(self):
        return self.item

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    
class Linkedlist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        first = Node(item)
        first.setNext(self.head)
        self.head = first

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and found is False:
            if current.getItem() is item:
                found = True
            else:
                current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getItem() is item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext()) 
        else:
            raise ValueError
            print(" Value not found")

    def insert(self, position, item):
        if position > self.size() - 1:
            raise IndexError
            print("Index out of bounds")
        current = self.head
        previous = None
        pos = 0
        if position == 0:
            self.add(item)
        else:
            first = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            previous.setNext(first)
            first.setNext(current)
        

    def index(self, item):
        current = self.head
        pos = 0
        found = False
        while current is not None and not found:
            if current.getItem() is item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position = None):
        if position > self.size():
            print("Index out of bound")
            raise IndexError

        current = self.head
        if position is None:
            ret = current.setItem()
            self.head = current.getNext()
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.getNext()
                pos += 1
                ret = current.getNext()
            previous.setNext(current.getNext())
            print(ret)
            return ret

    def append(self, item):
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            previous = current
            current = current.getNext()
            pos += 1
        first = Node(item)
        if previous is None:
            first.setNext(current)
            self.head = first
        else:
            previous.setNext(first)

    def printlist(self):
        current = self.head
        while current is not None:
            print(current.getItem())
            current = current.getNext()

l1 = Linkedlist()
l1.add('l')
l1.add('H')
l1.insert(1, 'e')
l1.append('l')
l1.append('o')
#l1.add(5)

l1.printlist()