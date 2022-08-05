class SmallChops:

    def __init__(self, ingredients):
        self.ingredients = ingredients
    #encapsulation
    def buns(self):
        print("i am round in shape, brown in color, and fluffy in texture")
        print('i am yummy and made of {}'.format(self.ingredients))

    def samosa(self):
        print("i am triangle in shape, and quite crunchy")
        print("i am a savoury snack and made of {}".format(self.ingredients))


#inheritance
class Snack(SmallChops):
    pass

Snack('Filling, flesh, egg, water').samosa()


