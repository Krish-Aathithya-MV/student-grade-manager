import sqlite3


connection = sqlite3.connect("students.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    roll_number TEXT PRIMARY KEY,
    marks TEXT
)
""")

connection.commit()


def add_student(name, roll_number):
    cursor.execute(
        """
        INSERT INTO students (name, roll_number, marks)
        VALUES (?, ?, ?)
        """,
        (name, roll_number, "")
    )
    connection.commit()


def get_all_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


def get_student(roll_number):
    cursor.execute(
        """
        SELECT * FROM students
        WHERE roll_number = ?
        """,
        (roll_number,)
    )
    return cursor.fetchone()


def add_mark(roll_number, mark):
    student = get_student(roll_number)

    if student is None:
        print("Student not found!")
        return

    current_marks = student[2]

    if current_marks == "":
        new_marks = str(mark)
    else:
        marks_list = current_marks.split(",")
        marks_list.append(str(mark))
        new_marks = ",".join(marks_list)

    cursor.execute(
        """
        UPDATE students
        SET marks = ?
        WHERE roll_number = ?
        """,
        (new_marks, roll_number)
    )

    connection.commit()


def delete_student(roll_number):
    cursor.execute(
        """
        DELETE FROM students
        WHERE roll_number = ?
        """,
        (roll_number,)
    )

    connection.commit()


def close_connection():
    connection.close()