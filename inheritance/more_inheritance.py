#Duck Typing - relates to inheritance and polymorphism 

class Duck:
    def swim(self):
        print('Swimming Duck')
    
    def fly(self):
        print("Flying Duck")
    

class Whale:
    def swim(self):
        print('Swimming Whale') 

animals = [Duck(), Duck(), Whale()]

for animal in animals:
    animal.swim()
    animal.fly()

