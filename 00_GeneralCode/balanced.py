# Version 1.0
class Balanced1:
    #inputt = input("Enter: ")

    def __init__(self):
        self.items = list(input("Enter: "))
        self.new = []

    def is_balanced(self):
        for item in self.items:
            if item == '(':
                self.new.append(item)
            try:
                if item == ')':
                    #if len(self.new) == 0:
                        #raise RuntimeError("Can't pop from an empty list")
                    self.new.pop()
            except IndexError:
                print("Can't pop from an empty list")
                return("An Unordered parenthesis")
                
        if len(self.new) == 0:
            return True
        else:
            return False



# Version 2.0
class Balanced2:
    #inputt = input("Enter: ")

    def __init__(self):
        self.items = list(input("Enter: "))
        self.new = []
        self.arranged = []

    def rearrange(self):
        for i in self.items:
            if i == '(':
                self.arranged.insert(0, i)
            else:
                self.arranged.append(i)

    def is_balanced(self):
        self.rearrange()
        for item in self.arranged:
            if item == '(':
                self.new.append(item)
            else:
                try:
                    self.new.pop()
                except IndexError:
                    return False  
        if len(self.new) == 0:
            return True
        else:
            return False



if __name__ == '__main__':
    select = input(" Select 1 for version 1 \n Select 2 for version 2: ")

    if select == 1:
        bal = Balanced1()
        print(bal.is_balanced())
    else:
        ba2 = Balanced2()
        print(ba2.is_balanced())