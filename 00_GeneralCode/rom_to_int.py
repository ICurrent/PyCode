def roman_to_int(rom):
    number = 0
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    for i in range(len(rom)-1):
        if roman[rom[i]] < roman[rom[i+1]]:
            number -= roman[rom[i]]
        else:
            number += roman[rom[i]]
    return number + roman[rom[-1]]


def int_to_rom(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,\
            100, 400, 500, 900, 1000]
    roman = "I IV V IX X XL L XC C CD D CM M"
    roman = roman.split()
    i = 12

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(roman[i], end='')
            div -= 1
        i -= 1


if __name__ == "__main__":
    roman = "DCXXI"
    print(roman_to_int(roman))
    #print()
    num = 621
    int_to_rom(num)