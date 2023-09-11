#These are different than "Instance Attributes" 
#Class attr and mehods act on the CLASS 

class Car:
    
    #Class attribute 
    #They go above all methods 
    number_of_cars = 0

    def __init__(self, make, model):
        self.make = make 
        self.model = model 
        #I added in this instance attr for testing -- if I call the class with the attr I get 5, if I use the instance attr of number_of_cars I get 0
        self.number_of_cars = 0
        #These are instance attributes 
        #When we use self - think instance 

        #Every time the Car class is instaniated it will increment the class attr by one - We can keep track of the number of instances from the Class Car 
        Car.number_of_cars += 1

    @classmethod
    #<cls> is mandatory for class methods - stands for name of the class 

    def set_number_of_cars(cls, cars):
        #cls == Car
        cls.number_of_cars = cars



car1 = Car("Porshe", "911")
car2 = Car("BMW", "X6")
car3 = Car("Honda", "Accord")

#Using the class method on the class -- class methods can only alter Class Attributes 
Car.set_number_of_cars(3)

#I can access the class attr from w/in the instance 
#print(car1.number_of_cars)

print(Car.number_of_cars)