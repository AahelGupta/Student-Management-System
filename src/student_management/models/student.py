class Student:
    student_id = 1
    def addStudent(self):
        self.id = Student.student_id
        Student.student_id += 1
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")
        self.email = input("Enter Email: ")
        self.phone = input("Enter Phone: ")
        self.address = input("Enter Address: ")
        self.grade = input("Enter Class/Grade: ")
    def displayStudent(self):
        print("\nStudent Details")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Address:", self.address)
        print("Grade:", self.grade)
    def updateStudent(self):
        self.name = input("New Name: ")
        self.age = int(input("New Age: "))
        self.email = input("New Email: ")
    def getData(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "grade": self.grade
        }