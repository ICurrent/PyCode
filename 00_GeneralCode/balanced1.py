# Version 1.0
class Balanced:
    inputt = input("Enter: ")

    def __init__(self):
        self.items = list(Balanced.inputt)
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

bal = Balanced()
print(bal.is_balanced())