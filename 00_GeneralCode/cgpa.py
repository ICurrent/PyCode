def cgpa_eva():
    try:
        no_of_semester = int(input("Enter the number of Semesters: "))
        print()
        totalUnits = []
        gottenUnits = []
        for _ in range(1, no_of_semester+1):  
            print(f"Semeter {_}:") 
            no_of_course = int(input("Enter the number of courses offered for this semester: "))
            for i in range(1, no_of_course+1):
                courses = input(f"Enter Course{i}: ")
                units = int(input(f"Enter the units of Course {i}: "))
                grading = {'A':4, 'B':3, 'C':2, 'D':1, 'E':0}  
                grade = int(input("Enter your score: "))
                if grade > 69:
                    grade = 'A'
                elif 60 <= grade < 70:
                    grade = 'B'
                elif 50 <= grade < 60:
                    grade = 'C'
                elif 45 <= grade < 50:
                    grade = 'D'
                else:
                    grade = 'E'

                gotten_units = units * grading[grade]
                gottenUnits.append(gotten_units)
                totalUnits.append(units*4)
                print()
        
        return f"CGPA: {round(sum(gottenUnits)*4/sum(totalUnits),2)}"
        
    except Exception:
        return "Input the right values"

    
        
print(cgpa_eva())