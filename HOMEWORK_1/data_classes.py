import json

class Person():
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super.__init__(name, age, email)
        self.student_id = student_id
    
def dataSaver(student):
    with open("studentData.json", "w"): as file:
        studentData = {
            'last_name': student.name.last_name(),
            'first_name': student.name.first_name(),
            'email': student.email,
            'student_id': student.student_id
        }
        json.dump(studentData)
