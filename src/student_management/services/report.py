class Report:
    def studentReport(self, students):
        print("\nStudent Report")
        for student in students:
            student.displayStudent()
    def attendanceReport(self, records):
        print("\nAttendance Report")
        for record in records:
            record.displayAttendance()
    def marksReport(self, marks):
        print("\nMarks Report")
        for m in marks:
            m.displayMarks()