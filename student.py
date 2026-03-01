# Student Record Management System

students = []   # List to store all student dictionaries


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to add student
def add_student():
    roll = input("Enter Roll Number: ")

    # Prevent duplicate roll numbers (Bonus Feature)
    for student in students:
        if student["roll"] == roll:
            print("Roll Number already exists! Student not added.")
            return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = sum(marks) / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


# Function to view all students
def view_students():
    if not students:
        print("No student records found.\n")
        return

    for student in students:
        print("---------------------------------")
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
    print("---------------------------------\n")


# Function to search student by roll number
def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            print()
            return

    print("Student not found.\n")


# Function to display class statistics
def class_statistics():
    if not students:
        print("No data available.\n")
        return

    total_students = len(students)

    class_total = 0
    highest = students[0]
    lowest = students[0]

    for student in students:
        class_total += student["average"]

        if student["total"] > highest["total"]:
            highest = student

        if student["total"] < lowest["total"]:
            lowest = student

    class_average = class_total / total_students

    print("----- Class Statistics -----")
    print("Total Students:", total_students)
    print("Class Average:", round(class_average, 2))
    print("Highest Scorer:", highest["name"], "-", highest["total"])
    print("Lowest Scorer:", lowest["name"], "-", lowest["total"])
    print()


# Main Menu using while loop
while True:
    print("===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Class Statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        class_statistics()
    elif choice == "5":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")



