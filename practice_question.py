class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("hana","20")
s2=Student("abel","22")
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)

class Car:
   def __init__(self,brand,color):
       self.brand=brand
       self.color=color
c1=Car("toyota","black")    
c2=Car("bmw","white")   
print(c1.brand)
print(c1.color)
print(c2.brand)
print(c2.color)

class student:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print("Hello, my name is", self.name)
stud=student("Hana")   
stud.introduce()

class University:
    school="Adiss Ababa University"
    def __init__(self,stud_name):
        self.stud_name=stud_name
# A class attribute is written inside the class but outside the methods.
stud1=   University("Hana")   
stud2= University("sara")

print(stud1.stud_name)
print(stud1.school)
print(stud2.stud_name)
print(stud2.school)

class BOOK:
    def __init__(self,title):
        self.title=title
    def __str__(self):
        return f"The is {self.title} written by jhon"
b1=BOOK("python basic")
print(b1)   

class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def __repr__(self):
        return f"phone('{self.brand}','{self.price}')"    
p1=Phone("samsung",15000)    
print(p1)

class STUDENT:
    university="Akiba Academy"
    def  __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department
    def display_info(self):
        print("Name:",self.name)
        print("age:",self.age)
        print("department:",self.department)
        print("university :",self.university)
    def __str__(self):
        return f"{self.name} studies IT"   
    def __repr__(self):
        return f"Student('{self.name}','{self.age}','{self.department}')"


ss1=STUDENT("Hana",20,"IT")
ss2=STUDENT("Mohamed",23,"Hafiz")

ss1.display_info()
ss2.display_info()
print(ss1)
print(repr(ss1))
