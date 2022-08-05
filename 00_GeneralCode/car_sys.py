name = input("Enter your name: ")

print(f'Hi! {name}, welcome to Current's Car rental system')
print()

class Rental:
    def __init__(self, list, name):
        self._carlist = list
        self._name = name
        self._lendDict = {}

    def Displaycars(self):
        print(f'List of cars available for rent are here:\n', self._name)
        for car in self._carlist:
            print(car)
    
    def Lendcar(self, user, car):
        if car  not in self._lendDict.keys():
            self._lendDict.update({car:user})
            print("Lender-car is updated in system, you can take car with you")
        else:
            print(f"car is already being used by {self._lendDict[car]}")

    def Addcar(self, car):
        if car not in self._carlist:
            self._carlist.append(car)
        else:
            pass
        print("Car database is updated now")

    def Returncar(self, car):
        self._lendDict.pop(car)
        print("Your car has been returned")

if __name__ == '__main__':
    rental = Rental(['Swift', 'Honda i 10', 'Swift Desire', 'Maruti'], 'Current car rental')

    while True:
        print(f'Welcome to the {rental._name} management')
        print("1. Displaycars")
        print("2. Lend a car")
        print("3. Add a car")
        print("4. Return a car")
        print("5. Exit")
        print()

        user_choice = int(input("Your choice?? "))
        if user_choice not in [1, 2, 3, 4, 5]:
            print("Not a valid choice, please choose again")
            break
        else:
            user_choice = user_choice

        if user_choice == 1:
            rental.Displaycars()
        elif user_choice == 2:
            print(f"car list {rental._carlist}")
            user = input("Enter your name: ")
            car = input("Enter the name of car you want: ")
            rental.Lendcar(user, car)
        elif user_choice == 3:
            car = input("Enter the car name: ")
            rental.Addcar(car)
        elif user_choice == 4:
            car = input("Enter the car you want to return: ")
            rental.Returncar(car)
        else:
            break