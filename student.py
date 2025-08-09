from db_config import get_connection

def add_student():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Enter name: ")
    program = input("Enter program: ")
    cur.execute("INSERT INTO students (name, program) VALUES (?, ?)", (name, program))
    conn.commit()
    conn.close()
    print("Student added successfully.")

def view_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    conn.close()

def update_student():
    conn = get_connection()
    cur = conn.cursor()
    student_id = input("Enter student ID to update: ")
    name = input("Enter new name: ")
    program = input("Enter new program: ")
    cur.execute("UPDATE students SET name = ?, program = ? WHERE id = ?", (name, program, student_id))
    conn.commit()
    conn.close()
    print("Student updated successfully.")

def delete_student():
    conn = get_connection()
    cur = conn.cursor()
    student_id = input("Enter student ID to delete: ")
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully.")
