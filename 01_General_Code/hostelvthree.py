import csv
from registrant import Student
new_applicants = []

file = open("comp_registration.csv","w")
submitter = csv.writer(file)
submitter.writerow(("name","hostel"))
for i in range(3):
    registrant_name = input("please enter your name:")
    registrant_dorm = input("please enter your the dorm you want:")
    new_applicants.append(Student(registrant_name, registrant_dorm))
submitter = csv.writer(file)
for sign_up in new_applicants:
    submitter.writerow((sign_up.registrant_name, sign_up.registrant_dorm))
enter = csv.writer(file)
enter.writerow(("chiyenre","moremi"))
enter = csv.writer(file)
enter.writerow(("bubu","nig"))
enter = csv.writer(file)
enter.writerow(("jide","compu"))
enter = csv.writer(file)
enter.writerow(("bunmi","owo"))

