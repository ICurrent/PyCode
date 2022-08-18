def roman_to_int(rom):
    number = 0
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    for i in range(len(rom)-1):
        if roman[rom[i]] < roman[rom[i+1]]:
            number -= roman[rom[i]]
        else:
            number += roman[rom[i]]
    return number + roman[rom[-1]]

if __name__ == "__main__":
    roman = "DCXXI"
    print(roman_to_int(roman))