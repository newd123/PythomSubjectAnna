class Student:

    def __init__(self, name, age, numberPhone):
        self.name = name
        self.age = age
        self.numberPhone = numberPhone
    def printer(self):
        print("Name of student",self.name)
        print("Age of student", self.age)
        print("numberPhone of student", self.numberPhone)
    def seconds(self):
        print("Seconds wich student life",self.age*365*24*60*60)


first_student = Student("Anna",20,"+380 (50) 678 34 12")
first_student.printer()
first_student.seconds()
print()
print()

second_student = Student("Ira",25,"+380 (50) 666 44 22")
second_student.printer()
second_student.seconds()
print()
print()