from registrant import Student
new_applicants = []
for i in range(3):
    registrant_name = input("please enter your name:")
    registrant_dorm = input("please enter your the dorm you want:")

    new_applicants.append(Student(registrant_name, registrant_dorm))

for sign_up in new_applicants:
    print("{} want this {} hostel".format(sign_up.registrant_name, sign_up.registrant_dorm))