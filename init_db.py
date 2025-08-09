import sqlite3

def initialize_db():
    conn = sqlite3.connect('university.db')
    cur = conn.cursor()

    cur.executescript("""
   CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    program TEXT NOT NULL
);

    CREATE TABLE IF NOT EXISTS instructors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        title TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS courses (
        course_number INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        credits INTEGER NOT NULL,
        syllabus TEXT,
        prerequisites TEXT
    );

    CREATE TABLE IF NOT EXISTS offerings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_number INTEGER,
        year INTEGER,
        semester TEXT,
        section INTEGER,
        instructor_id INTEGER,
        timings TEXT,
        classroom TEXT,
        FOREIGN KEY (course_number) REFERENCES courses(course_number),
        FOREIGN KEY (instructor_id) REFERENCES instructors(id)
    );

    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        offering_id INTEGER,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (offering_id) REFERENCES offerings(id)
    );
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully.")

if __name__ == '__main__':
    initialize_db()
