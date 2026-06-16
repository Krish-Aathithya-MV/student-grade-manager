import json
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def calculate_average(self):
        if len(self.marks) == 0:
            return None
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        avg = self.calculate_average()

        if avg is None:
            return "No marks yet"
        elif avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display_report(self):
        print("\n----------------------")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

        print("Marks:")
        if len(self.marks) == 0:
            print("No marks added yet.")
        else:
            for mark in self.marks:
                print(mark)

        avg = self.calculate_average()

        if avg is None:
            print("Average: No marks yet")
        else:
            print(f"Average: {avg:.2f}")

        print(f"Grade: {self.get_grade()}")
        print("----------------------\n")

    def to_dict(self):
        return{
            "name":self.name,
            "roll_number":self.roll_number,
            "marks":self.marks
        }


students = []


def find_student(roll_number):
    for student in students:
        if student.roll_number == roll_number:
            return student
    return None

def save_students():
    data = []
    for student in students:
        data.append(student.to_dict())

    with open("students.json","w") as file:
        json.dump(data, file, indent=4)

def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            for item in data:
                student = Student(
                    item["name"],
                    item["roll_number"]
                )

                student.marks = item["marks"]

                students.append(student)

    except FileNotFoundError:
        pass

load_students()


print("===== Student Grade Manager =====")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Add Marks")
    print("4. Generate Report")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 5.")
        continue

    if choice == 1:
        name = input("Enter student's name: ")
        roll_number = input("Enter roll number: ")

        if find_student(roll_number):
            print("Roll number already exists!")
        else:
            student = Student(name, roll_number)
            students.append(student)
            save_students()
            print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudents:")
            for student in students:
                print(f"{student.name} ({student.roll_number})")

    elif choice == 3:
        roll_number = input("Enter roll number: ")
        student = find_student(roll_number)

        if student:
            try:
                mark = int(input("Enter mark: "))

                if 0 <= mark <= 100:
                    student.marks.append(mark)
                    save_students()
                    print("Mark added successfully!")
                else:
                    print("Mark must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Student not found!")

    elif choice == 4:
        roll_number = input("Enter roll number: ")
        student = find_student(roll_number)

        if student:
            student.display_report()
        else:
            print("Student not found!")

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")