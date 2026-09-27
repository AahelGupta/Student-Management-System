class Course:
    course_id = 1
    def addCourse(self):
        self.id = Course.course_id
        Course.course_id += 1
        self.course_name = input("Course Name: ")
        self.teacher_name = input("Teacher Name: ")
        self.students = []
    def assignStudent(self, student_id):
        self.students.append(student_id)
    def displayCourse(self):
        print("\nCourse ID:", self.id)
        print("Course:", self.course_name)
        print("Teacher:", self.teacher_name)
        print("Students:", self.students)