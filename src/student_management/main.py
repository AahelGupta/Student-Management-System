from student import Student
from course import Course
from attendance import Attendance
from marks import Marks
from data import (students_data, courses_data, attendance_data, marks_data, course_assignments)
students = []
courses = []
attendance_records = []
marks_records = []
for data in students_data:
    s = Student()
    s.id = data[0]
    s.name = data[1]
    s.age = data[2]
    s.gender = data[3]
    s.email = data[4]
    s.phone = data[5]
    s.address = data[6]
    s.grade = data[7]
    students.append(s)
for data in courses_data:
    c = Course()
    c.id = data[0]
    c.course_name = data[1]
    c.teacher_name = data[2]
    c.students = []
    courses.append(c)
for assignment in course_assignments:
    student_id = assignment[0]
    course_id = assignment[1]
    for course in courses:
        if course.id == course_id:
            course.students.append(student_id)
            break
for data in attendance_data:
    a = Attendance()
    a.student_id = data[0]
    a.date = data[1]
    a.status = data[2]
    attendance_records.append(a)
for data in marks_data:
    m = Marks()
    m.student_id = data[0]
    m.subject = data[1]
    m.marks = data[2]
    marks_records.append(m)
Student.student_id = len(students) + 1
print("\n===== STUDENT MANAGEMENT SYSTEM =====")
print("1. Add Student")
print("2. View All Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. View Courses")
print("7. View Attendance")
print("8. View Marks")
print("9. Student Attendance Report")
print("10. Student Marks Report")
print("11. Top Students")
choice = int(input("\nEnter Choice: "))
if choice == 1:
    s = Student()
    s.addStudent()
    students.append(s)
    print("\nStudent Added Successfully")
    print("Student ID:", s.id)
elif choice == 2:
    for student in students:
        student.displayStudent()
elif choice == 3:
    sid = int(input("Enter Student ID: "))
    found = False
    for student in students:
        if student.id == sid:
            student.displayStudent()
            found = True
            break
    if not found:
        print("Student Not Found")
elif choice == 4:
    sid = int(input("Enter Student ID: "))
    found = False
    for student in students:
        if student.id == sid:
            student.updateStudent()
            print("Student Updated Successfully")
            found = True
            break
    if not found:
        print("Student Not Found")
elif choice == 5:
    sid = int(input("Enter Student ID: "))
    found = False
    for student in students:
        if student.id == sid:
            students.remove(student)
            print("Student Deleted Successfully")
            found = True
            break
    if not found:
        print("Student Not Found")
elif choice == 6:
    for course in courses:
        course.displayCourse()
elif choice == 7:
    for attendance in attendance_records:
        attendance.displayAttendance()
elif choice == 8:
    for mark in marks_records:
        mark.displayMarks()
elif choice == 9:
    sid = int(input("Enter Student ID: "))
    total = 0
    present = 0
    for record in attendance_records:
        if record.student_id == sid:
            total += 1
            if record.status.lower() == "present":
                present += 1
    if total > 0:
        percentage = (present / total) * 100
        print("Attendance Percentage:", round(percentage, 2), "%")
    else:
        print("No Attendance Record Found")
elif choice == 10:
    sid = int(input("Enter Student ID: "))
    total_marks = 0
    count = 0
    print("\nSubjects and Marks")
    for mark in marks_records:
        if mark.student_id == sid:
            print(mark.subject, ":", mark.marks)
            total_marks += mark.marks
            count += 1
    if count > 0:
        average = total_marks / count
        print("\nAverage Marks:", round(average, 2))
    else:
        print("No Marks Found")
elif choice == 11:
    student_marks = {}
    for mark in marks_records:
        sid = mark.student_id
        if sid not in student_marks:
            student_marks[sid] = []
        student_marks[sid].append(mark.marks)
    averages = []
    for sid in student_marks:
        avg = sum(student_marks[sid]) / len(student_marks[sid])
        averages.append([sid, avg])
    averages.sort(key=lambda x: x[1], reverse=True)
    print("\nTOP 10 STUDENTS")
    for student in averages[:10]:
        print("Student ID:", student[0], "Average Marks:", round(student[1], 2))
else:
    print("Invalid Choice")
print("\nProgram Terminated Successfully")