class S:
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
        self.__name = name

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
        animal_details = "{} is {} cm tall and {} kilogram and says {}".format(self.name, self.height, self.weight, self.sound)
        zoo_record = open("animal_details.txt", "w")
        zoo_record.write(animal_details)
        zoo_record.close()
        zoo_record = open("animal_details.txt", "a")
        zoo_record.write("\nnow am writing this in addition to that")
        zoo_record.close()
        zoo_record = open("animal_details.txt", "a")
        zoo_record.write("\nthis is the 3rd thing am writing here")
        zoo_record.close()
        zoo_record = open("animal_details.txt", "a")
        zoo_record.write("\nthis is the 4th thing am writing here")
        zoo_record.close()
        zoo_record = open("animal_details.txt", "a")
        zoo_record.write("\nthis is the 5th thing am writing here")
        zoo_record.close()

        return "{} is {} cm tall and {} kilogram and says {}".format(self.name, self.height, self.weight, self.sound)







#example 1:
cat = Animal("whisker", 30, 26, "meon")

cat.toString()
print(cat.toString())

chicken = Animal("fowl", 14, 12, "kookorokoo")
print(chicken.toString())



