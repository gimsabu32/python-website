class  Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def display_course_info(self):
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Students enrolled")
        for student in self.students:
            student.display_info()
            print("------")


#Creating Students Object
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)
student3 = Student("Charlie", 103)
#Creating a Course Object
course_python = Course("Python Programming", "PY101")
#Adding student to the course
course_python.add_student(student1)
course_python.add_student(student2)
course_python.add_student(student3)
#Displaying course_info
course_python.display_course_info()
