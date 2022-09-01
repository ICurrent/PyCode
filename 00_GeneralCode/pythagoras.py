def pythagoras(opposite, adjacent, hypotenus):
    try:
        if opposite == str('?'):
            return("Opposite = " + str(((hypotenus**2) - (adjacent**2))**0.5))

        if adjacent == str('?'):
            return("Adjacent = " + str(((hypotenus**2) - (opposite**2))**0.5))

        if hypotenus == str('?'):
            return("Hypotenus = " + str(((opposite**2) + (adjacent**2))**0.5))
    except ValueError:
        print("Invalid argument(s) were given. ")

print(pythagoras('?',4, 5))