# ExAample !
class University:
    # Constructor
    def __init__(self, name, year, location, type):
        self.name = name
        self.year = year
        self.location = location
        self.type = type
        self.hobbies = ''
        self.students = []

    def senateMembers(self):
        return f"The senate members of {self.name} are in charge of the school calendar"


class Person:
    firstName = input(" Enter your first name: ")
    lastName = input(" Enter your surname: ")
    age = int(input(" Enter your age: "))
    gender = input(" Enter your gender: ")

    def __init__(self, firstName, lastName, age, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender

    def get_bio_info(self):
        return f"This person is either a student or a lecturer."


class Faculty:
    #max_student = 0
    def __init__(self, faculty_name, max_no_student, max_no_lecturer):
        self.faculty = faculty_name
        self.max_no_student = max_no_student
        self.max_no_lecturer = max_no_lecturer
        self.students = []
        self.lecturer = []
        #Faculty.max_student += 1

    def enroll_stu(self, student):
        if len(self.students) < Faculty.max_student:
            self.students.append(student)
            return True
        return False
        
    def enroll_lect(self, lecturer):
        if len(self.lecturer) < self.max_no_lecturer:
            self.lecturer.append(lecturer)
            return True
        return False

class Lecturer(Person):
    lecturerID = input(" Enterv your ID: ")
    def __init__(self, firstName, lastName, age, gender, lecturerID):
        super().__init__(firstName, lastName, age, gender)
        self.LeturerID = lecturerID
        self.lecturer = []





uni_1 = University('University of Ibadan', '1928', 'Ibadan, Oyo State', 'Federal Institution')
print(uni_1.name)

p1 = Person('firstName', 'lastName', 'age', 'gender')
print(p1.get_bio_info())

f1 = Faculty('Engineering', 2, 2)

l1 = Lecturer('firstName', 'lastNAme', 'age', 'gender', 'lecturerID')
l2 = Lecturer('firstName', 'lastNAme', 'age', 'gender', 'lecturerID')
l3 = Lecturer('firstName', 'lastNAme', 'age', 'gender', 'lecturerID')


print(f1.enroll_lect(l1))
print(f1.enroll_lect(l2))
print(f1.enroll_lect(l3))
print(f1.lecturer)