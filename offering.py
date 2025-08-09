import sqlite3
from db_config import get_connection

def add_offering():
    conn = get_connection()
    cur = conn.cursor()
    course_number = input("Enter course number: ")
    year = input("Enter year: ")
    semester = input("Enter semester: ")
    section = input("Enter section number: ")
    instructor_id = input("Enter instructor ID: ")
    timings = input("Enter timings: ")
    classroom = input("Enter classroom: ")
    cur.execute("""INSERT INTO offerings 
        (course_number, year, semester, section, instructor_id, timings, classroom)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", 
        (course_number, year, semester, section, instructor_id, timings, classroom))
    conn.commit()
    print("✅ Offering added successfully.")
    conn.close()

def view_offerings():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM offerings")
    for row in cur.fetchall():
        print(row)
    conn.close()

def update_offering():
    conn = get_connection()
    cur = conn.cursor()
    offering_id = input("Enter offering ID to update: ")
    new_classroom = input("Enter new classroom: ")
    cur.execute("UPDATE offerings SET classroom = ? WHERE id = ?", (new_classroom, offering_id))
    conn.commit()
    print("✅ Offering updated successfully.")
    conn.close()

def delete_offering():
    conn = get_connection()
    cur = conn.cursor()
    offering_id = input("Enter offering ID to delete: ")
    cur.execute("DELETE FROM offerings WHERE id = ?", (offering_id,))
    conn.commit()
    print("🗑️ Offering deleted successfully.")
    conn.close()
