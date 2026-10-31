class Student:
    def __init__(self,name,age,department):
         self.name=name
         self.age=age
         self.department=department
    def  display_info(self):    
         print(f"name: {self.name}")
         print(f"age:{self.age}")
         print(f"department:{self.department}")
student1=Student("abebe","24","IT")         
student2=Student("kbede","23","IT") 

student1.display_info()
student2.display_info()