class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound
 #encapsulation
    def set_name(self, name):
        self.__name = input("please what is your name")

    def get_name(self):
        return self.name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.sound

    def get_type(self):
        print("Animal")
    def toString(self):
        return "{} is {} cm tall and {} kilogram and says {}".format(self.name, self.height, self.weight, self.sound)

class Dog(Animal):
    __owner = ""
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilogram and says {} and the owner is {}".format(self.name, self.height, self.weight, self.sound,
                                                                                         self.__owner)

spot = Dog("bingo", 34, 29, "whoof", "adeshina")
print(spot.toString())

#example 1:
cat = Animal("whisker", 30, 26, "meon")

cat.toString()
print(cat.toString())

chicken = Animal("fowl", 14, 12, "kookorokoo")
print(chicken.toString())



