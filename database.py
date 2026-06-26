import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    roll_number TEXT PRIMARY KEY
)
""")

# Marks table
cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_roll_number TEXT,
    mark INTEGER,
    FOREIGN KEY (student_roll_number)
        REFERENCES students(roll_number)
)
""")

connection.commit()




def add_student(name, roll_number):
    cursor.execute(
        """
        INSERT INTO students (name, roll_number)
        VALUES (?, ?)
        """,
        (name, roll_number)
    )

    connection.commit()


def get_all_students():
    cursor.execute(
        """
        SELECT *
        FROM students
        """
    )

    return cursor.fetchall()


def get_student(roll_number):
    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE roll_number = ?
        """,
        (roll_number,)
    )

    return cursor.fetchone()



def add_mark(roll_number, mark):
    if get_student(roll_number) is None:
        print("Student not found!")
        return

    cursor.execute(
        """
        INSERT INTO marks
        (student_roll_number, mark)
        VALUES (?, ?)
        """,
        (roll_number, mark)
    )

    connection.commit()


def get_marks(roll_number):
    cursor.execute(
        """
        SELECT mark
        FROM marks
        WHERE student_roll_number = ?
        """,
        (roll_number,)
    )

    rows = cursor.fetchall()

    return [row[0] for row in rows]




def get_average(roll_number):
    cursor.execute(
        """
        SELECT AVG(mark)
        FROM marks
        WHERE student_roll_number = ?
        """,
        (roll_number,)
    )

    return cursor.fetchone()[0]


def get_highest_mark(roll_number):
    cursor.execute(
        """
        SELECT MAX(mark)
        FROM marks
        WHERE student_roll_number = ?
        """,
        (roll_number,)
    )

    return cursor.fetchone()[0]


def get_lowest_mark(roll_number):
    cursor.execute(
        """
        SELECT MIN(mark)
        FROM marks
        WHERE student_roll_number = ?
        """,
        (roll_number,)
    )

    return cursor.fetchone()[0]


def get_marks_count(roll_number):
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM marks
        WHERE student_roll_number = ?
        """,
        (roll_number,)
    )

    return cursor.fetchone()[0]



def get_student_report(roll_number):
    cursor.execute(
        """
        SELECT students.name,
               marks.mark
        FROM students
        JOIN marks
        ON students.roll_number =
           marks.student_roll_number
        WHERE students.roll_number = ?
        """,
        (roll_number,)
    )

    return cursor.fetchall()




def delete_student(roll_number):
    cursor.execute(
        """
        DELETE FROM marks
        WHERE student_roll_number = ?
        """,
        (roll_number,)
    )

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