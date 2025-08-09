import student
import instructor
import course
import offering
import enrollment

def student_menu():
    while True:
        print("\n🔧 Student Menu")
        print("1. Add")
        print("2. View")
        print("3. Update")
        print("4. Delete")
        print("5. Back")
        c = input("Select: ")
        if c == '1': student.add_student()
        elif c == '2': student.view_students()
        elif c == '3': student.update_student()
        elif c == '4': student.delete_student()
        elif c == '5': break
        else: print("❌ Invalid option")

def instructor_menu():
    while True:
        print("\n👨‍🏫 Instructor Menu")
        print("1. Add")
        print("2. View")
        print("3. Update")
        print("4. Delete")
        print("5. Back")
        c = input("Select: ")
        if c == '1': instructor.add_instructor()
        elif c == '2': instructor.view_instructors()
        elif c == '3': instructor.update_instructor()
        elif c == '4': instructor.delete_instructor()
        elif c == '5': break
        else: print("❌ Invalid option")

def course_menu():
    while True:
        print("\n📘 Course Menu")
        print("1. Add")
        print("2. View")
        print("3. Update")
        print("4. Delete")
        print("5. Back")
        c = input("Select: ")
        if c == '1': course.add_course()
        elif c == '2': course.view_courses()
        elif c == '3': course.update_course()
        elif c == '4': course.delete_course()
        elif c == '5': break
        else: print("❌ Invalid option")

def offering_menu():
    while True:
        print("\n📅 Offering Menu")
        print("1. Add")
        print("2. View")
        print("3. Update")
        print("4. Delete")
        print("5. Back")
        c = input("Select: ")
        if c == '1': offering.add_offering()
        elif c == '2': offering.view_offerings()
        elif c == '3': offering.update_offering()
        elif c == '4': offering.delete_offering()
        elif c == '5': break
        else: print("❌ Invalid option")

def enrollment_menu():
    while True:
        print("\n📝 Enrollment Menu")
        print("1. Enroll Student")
        print("2. View Enrollments")
        print("3. Update Grade")
        print("4. Delete Enrollment")
        print("5. Back")
        c = input("Select: ")
        if c == '1': enrollment.enroll_student()
        elif c == '2': enrollment.view_enrollments()
        elif c == '3': enrollment.update_enrollment()
        elif c == '4': enrollment.delete_enrollment()
        elif c == '5': break
        else: print("❌ Invalid option")

def menu():
    while True:
        print("\n📚 University Registrar Menu")
        print("1. Manage Students")
        print("2. Manage Instructors")
        print("3. Manage Courses")
        print("4. Manage Course Offerings")
        print("5. Manage Enrollments")
        print("6. Exit")
        c = input("Select: ")
        if c == '1': student_menu()
        elif c == '2': instructor_menu()
        elif c == '3': course_menu()
        elif c == '4': offering_menu()
        elif c == '5': enrollment_menu()
        elif c == '6':
            print("👋 Exiting...")
            break
        else: print("❌ Invalid option")

if __name__ == "__main__":
    menu()
