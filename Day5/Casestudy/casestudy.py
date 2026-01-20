

# ---------- BASE CLASS ----------
class Person:
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    def get_details(self):
        return f"Name: {self.name}, Department: {self.department}"


# ---------- STUDENT CLASS ----------
class Student(Person):
    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):  # Polymorphism
        return f"Name: {self.name}, Role: Student, Department: {self.department}"

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 80 else "B"
        return avg, grade

    def __gt__(self, other):  # Operator overloading >
        return sum(self.marks) > sum(other.marks)


# ---------- FACULTY CLASS ----------
class Faculty(Person):
    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):  # Polymorphism
        return f"Name: {self.name}, Role: Faculty, Department: {self.department}"


# ---------- COURSE CLASS ----------
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):  # Operator overloading +
        return self.credits + other.credits


# ---------- MAIN PROGRAM ----------
students = []
faculty_list = []
courses = []

while True:
    print("\n--- Smart University Management System ---")
    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Calculate Student Performance")
    print("5. Compare Two Students")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dept = input("Department: ")
        sem = int(input("Semester: "))
        marks = list(map(int, input("Enter 5 marks separated by space: ").split()))
        s = Student(sid, name, dept, sem, marks)
        students.append(s)
        print("Student Created Successfully")

    elif choice == "2":
        fid = input("Faculty ID: ")
        name = input("Faculty Name: ")
        dept = input("Department: ")
        salary = int(input("Salary: "))
        f = Faculty(fid, name, dept, salary)
        faculty_list.append(f)
        print("Faculty Created Successfully")

    elif choice == "3":
        code = input("Course Code: ")
        cname = input("Course Name: ")
        credits = int(input("Credits: "))
        faculty_name = input("Faculty Name: ")
        course = Course(code, cname, credits, faculty_name)
        courses.append(course)
        print("Course Added Successfully")

    elif choice == "4":
        sid = input("Enter Student ID: ")
        for s in students:
            if s.pid == sid:
                avg, grade = s.calculate_performance()
                print("Student Performance Report")
                print("Name :", s.name)
                print("Average :", avg)
                print("Grade :", grade)
                break
        else:
            print("Student not found")

    elif choice == "5":
        if len(students) >= 2:
            s1 = students[0]
            s2 = students[1]
            print(f"Comparing {s1.name} > {s2.name} :", s1 > s2)
        else:
            print("Need at least 2 students")

    elif choice == "6":
        print("Thank you for using Smart University Management System")
        break

    else:
        print("Invalid choice")
