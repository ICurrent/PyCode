# Find upper case and lower case letters in any string

def string_sorter(text):
    count_string = {"Uppercase" : 0, "Lowercase" : 0}
    upper_letter = []
    lower_letter = []
    
    for letter in text:
        if letter.isupper():
            count_string['Uppercase'] += 1
            upper_letter.append(letter)
        elif letter.islower():
            count_string['Lowercase'] += 1
            lower_letter.append(letter)
        else:
            pass
    print("Statement was: ", text)
    print("Count of upper and lower case", count_string)
    print("Lists of upper and lower letters: ", upper_letter, lower_letter)


string_sorter("Welcome to the World of Possibilities")