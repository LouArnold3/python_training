#Does not have access to self / cls attr. Static methods just belong to the class 
#Better organize and keep code together 

class Student:

    #Class / Static Attribute are the same 
    num_of_student = 0
    grade_bump = 2.0

    def __init__(self, name, grades=[]):
        self.name = name 
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod
    def avg_of_grade_plus_bump(cls, grades):
        return cls.avg_of_grade_plus_bump(grades) + cls.grade_bump 

    @staticmethod
    #The static class decorator 
    def average_from_grades(grades):
        return sum(grades) / len(grades)
    

        
    

s1 = Student("Lou", [100, 100, 99])
s2 = Student("Arnold", [78, 88, 65])

#We can call static methods on an instance of Student OR directly on the class 
average = s1.average_from_grades(s2.grades)
print(average)

#Class method has access to things that are part of the class. The static does not.