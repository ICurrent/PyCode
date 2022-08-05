import sys
import os
nov_file = open("nov.txt", "w")
nov_file.close()
nov_file = open("nov.txt", "w")
nov_file.write("yes this nov, we have alot to learn at compudemic")
nov_file.close()
nov_file = open("nov.txt", "a")
nov_file.write("ynow i dont want to loose what i have writen before")
nov_file.close()
nov_file = open("nov.txt", "r")
todays_class = nov_file.read()
print(todays_class)
nov_file.close()
print(todays_class)

