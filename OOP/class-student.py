class Student:
    number_of_students = 0
    school = "College of Engineering"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.number_of_students += 1

    def name_age(self):
        return f'Name: {self.name}, age: {self.age}'
    def name_school(self):
        return f'Name: {self.name}, school: {self.school}'
    @classmethod
    def set_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        name, age, school = student_str.split('.')
        return cls(name,age)

print(Student.number_of_students)
student1 = Student("John", 20)
student2 = Student("Jane", 30)

print(student1.name_age())
print(Student.name_age(student2))
print(student1.name_school())
print(student2.name_school())
print(Student.number_of_students)
new_student = 'Jose.19.English'
student3 = Student.split_students(new_student)
print(student3.name_age())

Student.set_school("College of Arts")
print(student3.name_school())
print(Student.number_of_students)