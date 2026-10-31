# class Dog:
#     def bark(self):
#         print("woof")
# d1=Dog()        
class Car:
    def __init__(self,brand,color,):
        self.brand=brand
        self.color=color
        speed=0
    def accelarate(self):
        self.speed+=5
        print(f"speed:{self.speed}")

car1= Car("totyota","red")
car2= Car("BYD","Blue")

print(car1.color)
print(car2.brand)
class Phone:
        def __init__(self,brand):
             self.brand=brand
phone1=Phone("samsung") 
phone2=Phone("apple")   
print(phone1.brand)    
print(phone2.brand)  
class Student:
     company ="akiba"

     def __init__(self,name):
          self.name=name

s1=Student("abdurahim")
s2=Student("muhammed")
s1.company="Another company"
print(s1.company)
print(s2.company)
print(Student.company)

class Point:
     def __init__(self , x,y):
         self.x=x
         self.y=y
     def __str__(self):
         return f"({self.x},{self.y})" 
     def __repr__(self):
         
             return f"({self.x},{self.y})" 
p = Point(1,2)     
print(p)
print(repr(p))
# class Rectangle :
#      def __init__(self,height,width):
#           self.height=height
#           self.width=width
#      def area(self):
#           return self.width*self.height
#      def perimeter(self):
#             return 2* (self.width+self.height )
#      def __str__(self):
#           return f"Rectangle({self.width}x{self.width})"
     
# r1=Rectangle(3,4)
# r2=Rectangle(5,6)
# r3=Rectangle(6,8)

# for rectangle in (r1,r2,r3):
#      print(rectangle)
#      print("Area :",rectangle.area)
#      print("perimeter :",rectangle.perimeter)
#A class is like a plan or design. It describes what an object should have and what it can do.
class Studentt:
      def __init__(self,name):
          self.name=name
ss1=Studentt("hana")
ss2=Studentt("Abel")        
print(ss1.name)
print(ss2.name)