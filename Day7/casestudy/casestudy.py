import csv
from abc import ABC, abstractmethod

# DESCRIPTOR (Marks Validation)

class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks must be between 0 and 100")
        instance._marks = value

# ABSTRACT BASE CLASS
class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

# STUDENT CLASS

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):
        return f"Student Name: {self.name}, Department: {self.department}"

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    # Operator Overloading (>)
    def __gt__(self, other):
        return self.calculate_performance()[0] > other.calculate_performance()[0]

# FACULTY CLASS
class Faculty(Person):
    def __init__(self, fid, name, department):
        super().__init__(fid, name, department)

    def get_details(self):
        return f"Faculty Name: {self.name}, Department: {self.department}"

# COURSE CLASS

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

# STORAGE

students = []
faculties = []
courses = []
enrollments = {}

# MENU FUNCTIONS

def add_student():
    try:
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dept = input("Enter Department: ")
        sem = int(input("Enter Semester: "))
        marks = list(map(int, input("Enter 5 marks (space separated): ").split()))

        student = Student(sid, name, dept, sem, marks)
        students.append(student)

        print("\nStudent Created Successfully")
        print("----------------------------")
        print("ID        :", sid)
        print("Name      :", name)
        print("Department:", dept)
        print("Semester  :", sem)

    except Exception as e:
        print("Error:", e)

def add_faculty():
    fid = input("Enter Faculty ID: ")
    name = input("Enter Faculty Name: ")
    dept = input("Enter Department: ")

    faculty = Faculty(fid, name, dept)
    faculties.append(faculty)

    print("\nFaculty Created Successfully")
    print("----------------------------")
    print("ID        :", fid)
    print("Name      :", name)
    print("Department:", dept)

def add_course():
    code = input("Enter Course Code: ")
    name = input("Enter Course Name: ")
    credits = int(input("Enter Credits: "))
    fid = input("Enter Faculty ID: ")

    faculty = next((f for f in faculties if f.pid == fid), None)

    if faculty:
        course = Course(code, name, credits, faculty)
        courses.append(course)

        print("\nCourse Added Successfully")
        print("-------------------------")
        print("Course Code:", code)
        print("Course Name:", name)
        print("Credits    :", credits)
        print("Faculty    :", faculty.name)
    else:
        print("Faculty not found")

def enroll_student_to_course():
    sid = input("Enter Student ID: ")
    code = input("Enter Course Code: ")

    student = next((s for s in students if s.pid == sid), None)
    course = next((c for c in courses if c.code == code), None)

    if student and course:
        enrollments[sid] = course.name
        print("\nEnrollment Successful")
        print("---------------------")
        print("Student Name:", student.name)
        print("Course      :", course.name)
    else:
        print("Student or Course not found")

def calculate_performance():
    sid = input("Enter Student ID: ")
    student = next((s for s in students if s.pid == sid), None)

    if student:
        avg, grade = student.calculate_performance()
        print("\nStudent Performance Report")
        print("--------------------------")
        print("Student Name:", student.name)
        print("Marks       :", student.marks)
        print("Average     :", avg)
        print("Grade       :", grade)
    else:
        print("Student not found")

def compare_students():
    s1 = input("Enter First Student ID: ")
    s2 = input("Enter Second Student ID: ")

    st1 = next((s for s in students if s.pid == s1), None)
    st2 = next((s for s in students if s.pid == s2), None)

    if st1 and st2:
        print("\nComparing Students Performance")
        print("------------------------------")
        print(f"{st1.name} > {st2.name} :", st1 > st2)
    else:
        print("Student not found")

# GENERATE REPORTS

def generate_reports():
    if not students:
        print("No student data available")
        return

    try:
        file_exists = False
        try:
            with open("students_report.csv", "r"):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open("students_report.csv", "a", newline="") as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(["ID", "Name", "Department", "Semester", "Average", "Grade"])

            for s in students:
                avg, grade = s.calculate_performance()
                writer.writerow([s.pid, s.name, s.department, s.semester, avg, grade])

        print("\nCSV Report Updated Successfully")
        print("File Name: students_report.csv")
        students.clear()

    except Exception as e:
        print("Error generating report:", e)
# MAIN MENU (EXACTLY AS CASE STUDY)


def menu():
    while True:
        print("""
1 -> Add Student
2 -> Add Faculty
3 -> Add Course
4 -> Enroll Student to Course
5 -> Calculate Student Performance
6 -> Compare Two Students
7 -> Generate Reports
8 -> Exit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_faculty()
        elif choice == "3":
            add_course()
        elif choice == "4":
            enroll_student_to_course()
        elif choice == "5":
            calculate_performance()
        elif choice == "6":
            compare_students()
        elif choice == "7":
            generate_reports()
        elif choice == "8":
            print("\nThank you for using Smart University Management System")
            break
        else:
            print("Invalid choice")
menu()
