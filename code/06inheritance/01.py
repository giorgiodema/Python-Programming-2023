class Person:
    def __init__(self,name:str,surname:str):
        self.name = name
        self.surname = surname

    def printInfo(self):
        print(f"name:{self.name},surname:{self.surname}")

    def __str__(self):
        return f"{self.name},{self.surname}"
    
class Student(Person):
    def __init__(self, name: str, surname: str, student_id:str):
        super().__init__(name, surname)
        self.student_id = student_id

    def printInfo(self):
        print(f"name:{self.name},surname:{self.surname},student_id:{self.student_id}")

    def __str__(self):
        return super().__str__() + f",{self.student_id}"
    

p = Person("Mario","Rossi")
print(p)
p.printInfo()

s = Student("Luigi","Bianchi","1234567")
print(s)
s.printInfo()
print(s.name)

print(p.student_id)
