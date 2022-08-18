# Version 2.0
class Balanced:
    inputt = input("Enter: ")

    def __init__(self):
        self.items = list(Balanced.inputt)
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
    bal = Balanced()
    print(bal.is_balanced())