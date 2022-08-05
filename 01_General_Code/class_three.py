#creating class functions, methods, and inheritance
class Person:
    #creating __init__ in a class make the class a FUNCTION that can be called wih arguments
    #other def functions in a class asides from (__init__ def funtion) are basically subfunctions otherwise called METHODS
    #SAMPLE:  Function.method
    #sample: Person(name).talk
    #sample2: Person(name).greet
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('i dey talk to  {}'.format(self.name))

    def greet(self):
        print('i no dey talk but but just dey greet '.format(self.name))


fan = Person('john')
fan.talk()
Person('titi').talk()
Person('faysal').greet()


#INHERITANCE
#when same methods apply to different classes, create the methods in just one class, and make other classes inherit the methods
#in that one class.
#example below

class Mammal:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print('{} walks'.format(self.name))

#Human inherits methods/function in Mammal
class Human(Mammal):
    pass

#Ape inherits methods/function in Mammal
class Ape(Mammal):
    pass

Mammal('goat').walk()
Human('NINI').walk()
Ape('NIGER').walk()