#class instantiation
class postgraduate:
    name = input("please enter your name:")
    matricNo = input("please enter your matric no:")
    dept = input("please enter your dept:")
    gender = input("please enter your gender:")
    level = input("please enter your level:")
#class constructor

    def __init__(self, name, matricNo, dept, gender,level):
        self.__name = name
        self.__matricNo = matricNo
        self.__dept = dept
        self.__gender = gender
        self.__level = level
# class encapsulation
    def set_name(self, name):# class setters or accessor
        self.__name = name

    def get_name(self):# class getter or mutators
        return self.__name

    def set_matricNo(self, matricNo):# class setters or accessor
        self.__matricNo = matricNo

    def get_matricNo(self):# class getter or mutators
        return self.__matricNo

    def set_dept(self, dept):# class setters or accessor
        self.__dept = dept

    def get_dept(self):# class getter or mutators
        return self.__dept

    def set_gender(self, gender):# class setters or accessor
        self.__gender = gender

    def get_gender(self):# class getter or mutators
        return self.__gender

    def set_leve(self, level):# class setters or accessor
        self.__level = level

    def get_level(self):# class getter or mutators
        return self.__level
# class fixed instant caller
    #def get_type(self):
        #print("undergraduate")

# class instant caller
    def toString(self):
       return "{} whose matric number is {}  is in {} and a {} is a {} level student"\
           .format(self.name, self.matricNo, self.dept, self.gender,self.level)

#class referencing
student_one = postgraduate('name', 'matricNo', 'dept', 'gender', 'level')

student_one.toString()
print(student_one.toString())
print(student_one.get_level())

print(student_one.name)

