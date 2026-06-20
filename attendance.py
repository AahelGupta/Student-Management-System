class Attendance:
    def markAttendance(self):
        self.student_id = int(input("Student ID: "))
        self.date = input("Date: ")
        self.status = input("Present/Absent: ")
    def displayAttendance(self):
        print(self.student_id, self.date,self.status)