class Student:
    total = 0
     
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
        self.courses = []
        self.average = 0
        
        
    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def add_grade(self, name, grade):
        self.grades[name] = grade

    def calculate_average(self):
        for x in self.grades:
            self.total += x
        self.average = self.total / len(self.grades)

    def display_info(self):
        print("--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")

        print("Courses: ")
        for x in self.courses:
            print(f"- {x}")
        print("Grades:")

        for key, value in self.grades.items():
            print(f"{key}: {value}")

        print(f"Average: {self.average}")

student = Student("Michael", "C5001")

student.add_course("Python")
student.add_course("Mathematics")

student.add_grade("Python", 85)
student.add_grade("Mathematics", 72)


student.display_info()