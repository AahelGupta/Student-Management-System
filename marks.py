class Marks:
    def addMarks(self):
        self.student_id = int(input("Student ID: "))
        self.subject = input("Subject: ")
        self.marks = float(input("Marks: "))
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"
    def displayMarks(self):
        print("\nStudent ID:", self.student_id)
        print("Subject:", self.subject)
        print("Marks:", self.marks)
        print("Grade:", self.grade())