class Student:
    school_name="Akiba_Academy"
    def __init__(self,name,score,department):
         self.name=name
         self.score=score
         self.department=department
    def    display(self):
         print("Name:",self.name)
         print("score:",self.score)
         print("Dpartment:",self.department)
         print("school_name:",self.school_name)

s1=Student("Husni","A","IT")         
s2=Student("Meryem","A+","doctor")
s3=Student("Mohamed","A+","Hafiz(")
s1.score="A+"
s1.display()
s2.display()
s3.display()