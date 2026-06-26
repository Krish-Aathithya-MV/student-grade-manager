import database


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

        if database.get_student(roll_number):
            print("Roll number already exists!")
        else:
            database.add_student(name, roll_number)
            print("Student added successfully!")


    elif choice == 2:
        students = database.get_all_students()

        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudents:")
            for student in students:
                print(f"{student[0]} ({student[1]})")


    elif choice == 3:
        roll_number = input("Enter roll number: ")

        if database.get_student(roll_number):
            try:
                marks_input = input(
                    "Enter marks separated by commas: "
                )

                marks = [
                    m.strip()
                    for m in marks_input.split(",")
                ]

                added_count = 0

                for mark in marks:
                    mark = int(mark)

                    if 0 <= mark <= 100:
                        database.add_mark(
                            roll_number,
                            mark
                        )
                        added_count += 1
                    else:
                        print(
                            f"{mark} is invalid. "
                            "Marks must be between 0 and 100."
                        )

                if added_count > 0:
                    print(
                        f"{added_count} mark(s) added successfully!"
                    )

            except ValueError:
                print(
                    "Please enter valid numbers "
                    "(example: 85,90,76)."
                )
        else:
            print("Student not found!")


    elif choice == 4:
        roll_number = input(
            "Enter roll number: "
        )

        student = database.get_student(
            roll_number
        )

        if student:
            name = student[0]
            roll = student[1]

            temp_student = Student(
                name,
                roll
            )

            temp_student.marks = (
                database.get_marks(
                    roll_number
                )
            )

            temp_student.display_report()

        else:
            print("Student not found!")


    elif choice == 5:
        database.close_connection()
        print("Goodbye!")
        break

    else:
        print(
            "Invalid choice. "
            "Please enter a number from 1 to 5."
        )