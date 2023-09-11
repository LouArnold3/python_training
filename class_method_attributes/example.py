class Circle:

    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)
    
    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius
    
    @classmethod
    def get_area_and_perimeter(cls, radius):
        return cls.area(radius), cls.perimeter(radius)

# Modify one class attr and apply to all methods 

print(Circle.area(2))
print(Circle.perimeter(2))
print(Circle.get_area_and_perimeter(2))

