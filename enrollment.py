from db_config import get_connection

def enroll_student():
    conn = get_connection()
    cur = conn.cursor()
    student_id = input("Enter student ID: ")
    offering_id = input("Enter offering ID: ")
    grade = input("Enter grade (or leave blank): ")
    cur.execute("INSERT INTO enrollments (student_id, offering_id, grade) VALUES (?, ?, ?)",
                (student_id, offering_id, grade if grade else None))
    conn.commit()
    conn.close()
    print("✅ Student enrolled successfully.")

def view_enrollments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM enrollments")
    for row in cur.fetchall():
        print(row)
    conn.close()

def update_enrollment():
    conn = get_connection()
    cur = conn.cursor()
    id_ = input("Enter enrollment ID to update: ")
    grade = input("Enter new grade: ")
    cur.execute("UPDATE enrollments SET grade = ? WHERE id = ?", (grade, id_))
    conn.commit()
    conn.close()
    print("✅ Enrollment updated successfully.")

def delete_enrollment():
    conn = get_connection()
    cur = conn.cursor()
    id_ = input("Enter enrollment ID to delete: ")
    cur.execute("DELETE FROM enrollments WHERE id = ?", (id_,))
    conn.commit()
    conn.close()
    print("🗑️ Enrollment deleted successfully.")
