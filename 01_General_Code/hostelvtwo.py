import csv
from registrant import Student
new_applicants = []
for i in range(2):
    registrant_name = input("please enter your name:")
    registrant_dorm = input("please enter your the dorm you want:")

    new_applicants.append(Student(registrant_name, registrant_dorm))

file = open("room_registration.csv","w")
submitter = csv.writer(file)
for sign_up in new_applicants:
    submitter.writerow((sign_up.registrant_name, sign_up.registrant_dorm))
file.close()