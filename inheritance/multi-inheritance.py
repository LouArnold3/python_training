class A:
    def __init__(self) -> None:
        print("A")

class B():
    def __init__(self) -> None:
        print("B")

class C(A, B):
#C is the child class 
    def __init__(self):
        #We added in this super init method - what will print now? A or B -> B..... it was "A"
        super().__init__()
        

#What would print from this object? "A" because it is defined first 
c = C()
print(isinstance(c, A))


#MRO - Method Resolution Order - start by looking in main class then look in the 1st super class and then the 2nd super class 