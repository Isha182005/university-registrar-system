from db_config import get_connection

def add_course():
    conn = get_connection()
    cur = conn.cursor()
    course_number = input("Enter course number: ")
    title = input("Enter course title: ")
    credits = int(input("Enter number of credits: "))
    syllabus = input("Enter syllabus: ")
    prerequisites = input("Enter prerequisites (comma-separated course numbers): ")
    cur.execute("INSERT INTO courses (course_number, title, credits, syllabus, prerequisites) VALUES (?, ?, ?, ?, ?)",
                (course_number, title, credits, syllabus, prerequisites))
    conn.commit()
    conn.close()
    print("✅ Course added successfully.")

def view_courses():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    for row in cur.fetchall():
        print(row)
    conn.close()

def update_course():
    conn = get_connection()
    cur = conn.cursor()
    course_number = input("Enter course number to update: ")
    title = input("Enter new title: ")
    credits = int(input("Enter new number of credits: "))
    syllabus = input("Enter new syllabus: ")
    prerequisites = input("Enter new prerequisites: ")
    cur.execute("UPDATE courses SET title = ?, credits = ?, syllabus = ?, prerequisites = ? WHERE course_number = ?",
                (title, credits, syllabus, prerequisites, course_number))
    conn.commit()
    conn.close()
    print("✅ Course updated successfully.")

def delete_course():
    conn = get_connection()
    cur = conn.cursor()
    course_number = input("Enter course number to delete: ")
    cur.execute("DELETE FROM courses WHERE course_number = ?", (course_number,))
    conn.commit()
    conn.close()
    print("🗑️ Course deleted successfully.")
