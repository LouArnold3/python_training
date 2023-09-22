# Inheritance = OOP Concept that states that once class can inherit the functionality of another class 
#Have related classes in program - have related classes to reuse functionality - reduces duplication 
#Polymorphism - many forms You can treat a manager as a manager and an employee 

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def print_hello(self):
        return f"Hello, my name is {self.first_name} {self.last_name}"



class Employee(Person):
    #Constructor Override 
    def __init__(self, first_name, last_name, salary):
        #user the super() method to access the constructor and override
        super().__init__(first_name, last_name)
        self.salary = salary 
    #I want this class to have some functionality from the Person class - I could just cope the methods over but what is not best practice
    #I can add the Person class as a param to the Employee class 
    #Employee is called the Child/Derived/Sub Class -- the Person class is the Parent/Base/Super Class
    def test(self):
        print("test")

    def print_hello(self):
        #You can access methods from the super/parent class using the super() method following the method
        #Aka Method Override 
        x = super().print_hello()
        print(x +"!" + f"I make {self.salary} per year")


class Manager(Employee):
    #Test : Override the constructor and add in a department attribute 
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department

class Owner(Person):
    def __init__(self, first_name, last_name, networth):
        super().__init__(first_name, last_name)
        self.networth = networth


m = Manager("Louis", "Arnold", 100000, 'cyber')
o = Owner("Lou", "Arnold", 100000000000)

#With this inheritsance we will run the print_hello method inside of the Person class bc Person is the Parent class 
print(o.print_hello())
#The isinstance() function : Check to see if an object is an Instance of a class and returns a boolean 
print(isinstance(o, Employee))


#p = Person("Joe", "Blank")
#m.print_hello()








