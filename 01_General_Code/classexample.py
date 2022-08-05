class Mammals:

    def __init__(self, name, sound, region):
        self.name = name
        self.sound = sound
        self.region = region

#encapsulation
    def talk(self):
        print('hi, i am {}, i make sounds like {}, and i am from {}'.format(self.name, self.sound, self.region))

    def greet(self):
        print('hey {}, whatsup'.format(self.name))

Mammals('flour, water, sugar', 'talking', 'africa').talk()

human = Mammals('human', 'talking', 'africa')

human.talk()

#inheritance

class Shark(Mammals):
    pass


Shark('baby shark', 'meow', 'atlantic ocean').talk()


