import os
import csv
from student import Student
students = []
for i in range (3):
    name = input("please enter your name:")
    dorm = input("please enter your dorm:")

    students.append(Student(name, dorm))

file = open("frid.csv", "w")
writer = csv.writer(file)
for student in students:
    writer.writerow((student.name, student.dorm))
file.close()

#os.remove("students.csv")



