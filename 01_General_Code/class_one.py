#class instantiation
class undergraduate:
    __name = ""
    __matricNo = ""
    __dept = ""
    __gender = ""
    __level = 0
#class constructor

    def __init__(self, name, matricNo, dept, gender,level):
        self.name = name
        self.matricNo = matricNo
        self.dept = dept
        self.gender = gender
        self.level = level
# class encapsulation
    def set_name(self, name):# class setters or accessor
        self.__name = name

    def get_name(self):# class getter or mutators
        return self.name

    def set_matricNo(self, matricNo):# class setters or accessor
        self.__matricNo = matricNo

    def get_matricNo(self):# class getter or mutators
        return self.matricNo

    def set_dept(self, dept):# class setters or accessor
        self.__dept = dept

    def get_dept(self):# class getter or mutators
        return self.dept

    def set_gender(self, gender):# class setters or accessor
        self.__gender = gender

    def get_gender(self):# class getter or mutators
        return self.gender

    def set_leve(self, level):# class setters or accessor
        self.__level = level,

    def get_level(self):# class getter or mutators
        return self.level
# class fixed instant caller
    #def get_type(self):
        #print("undergraduate")

# class instant caller
    def toString(self):
       return "{} whose matric number is {}  is in {} and a {} is a {} level student"\
           .format(self.name, self.matricNo, self.dept, self.gender,self.level)

#class referencing

student_one = undergraduate('maryle','45680','English','female','400')
student_one.toString()
print(student_one.toString())
######print(student_one)



