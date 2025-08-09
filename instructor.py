from db_config import get_connection

def add_instructor():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Enter name: ")
    department = input("Enter department: ")
    title = input("Enter title: ")
    cur.execute("INSERT INTO instructors (name, department, title) VALUES (?, ?, ?)",
                (name, department, title))
    instructor_id = cur.lastrowid
    conn.commit()
    conn.close()
    print(f"✅ Instructor added successfully with ID: {instructor_id}")

def view_instructors():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM instructors")
    rows = cur.fetchall()
    print("\n📋 All Instructors:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Department: {row[2]}, Title: {row[3]}")
    conn.close()

def update_instructor():
    conn = get_connection()
    cur = conn.cursor()
    instructor_id = input("Enter instructor ID to update: ")
    name = input("Enter new name: ")
    department = input("Enter new department: ")
    title = input("Enter new title: ")
    cur.execute("UPDATE instructors SET name = ?, department = ?, title = ? WHERE id = ?",
                (name, department, title, instructor_id))
    conn.commit()
    conn.close()
    print("✅ Instructor updated successfully.")

def delete_instructor():
    conn = get_connection()
    cur = conn.cursor()
    instructor_id = input("Enter instructor ID to delete: ")
    cur.execute("DELETE FROM instructors WHERE id = ?", (instructor_id,))
    conn.commit()
    conn.close()
    print("🗑️ Instructor deleted successfully.")
