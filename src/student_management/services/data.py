students_data = [
    [1, "Rahul Sharma", 20, "Male", "rahul@gmail.com", "9876543210", "Kolkata", "BCA"],
    [2, "Priya Das", 19, "Female", "priya@gmail.com", "9876543211", "Howrah", "BCA"],
    [3, "Amit Roy", 21, "Male", "amit@gmail.com", "9876543212", "Durgapur", "BCA"],
    [4, "Sneha Paul", 20, "Female", "sneha@gmail.com", "9876543213", "Siliguri", "BCA"],
    [5, "Arjun Sen", 22, "Male", "arjun@gmail.com", "9876543214", "Kharagpur", "BCA"],
    [6, "Riya Ghosh", 19, "Female", "riya@gmail.com", "9876543215", "Asansol", "BCA"],
    [7, "Sourav Dey", 21, "Male", "sourav@gmail.com", "9876543216", "Malda", "BCA"],
    [8, "Ananya Bose", 20, "Female", "ananya@gmail.com", "9876543217", "Bardhaman", "BCA"],
    [9, "Vikram Gupta", 22, "Male", "vikram@gmail.com", "9876543218", "Haldia", "BCA"],
    [10, "Pooja Singh", 19, "Female", "pooja@gmail.com", "9876543219", "Darjeeling", "BCA"]
]
courses_data = [
    [1, "Python Programming", "Mr. Mukherjee"],
    [2, "Database Management System", "Mrs. Banerjee"],
    [3, "Data Structures", "Mr. Ghosh"]
]
course_assignments = [
    [1, 1], [2, 2], [3, 3], [4, 1], [5, 2],
    [6, 3], [7, 1], [8, 2], [9, 3], [10, 1]
]
attendance_data = [
    [1, "2026-06-01", "Present"], [1, "2026-06-02", "Present"], [1, "2026-06-03", "Present"], [1, "2026-06-04", "Present"], [1, "2026-06-05", "Present"],
    [1, "2026-06-06", "Present"], [1, "2026-06-07", "Present"], [1, "2026-06-08", "Present"], [1, "2026-06-09", "Present"], [1, "2026-06-10", "Absent"],
    [2, "2026-06-01", "Present"], [2, "2026-06-02", "Present"], [2, "2026-06-03", "Present"], [2, "2026-06-04", "Present"], [2, "2026-06-05", "Present"],
    [2, "2026-06-06", "Present"], [2, "2026-06-07", "Present"], [2, "2026-06-08", "Present"], [2, "2026-06-09", "Absent"], [2, "2026-06-10", "Absent"],
    [3, "2026-06-01", "Present"], [3, "2026-06-02", "Present"], [3, "2026-06-03", "Present"], [3, "2026-06-04", "Present"], [3, "2026-06-05", "Present"],
    [3, "2026-06-06", "Present"], [3, "2026-06-07", "Present"], [3, "2026-06-08", "Present"], [3, "2026-06-09", "Present"], [3, "2026-06-10", "Present"],
    [4, "2026-06-01", "Present"], [4, "2026-06-02", "Present"], [4, "2026-06-03", "Present"], [4, "2026-06-04", "Present"], [4, "2026-06-05", "Present"],
    [4, "2026-06-06", "Present"], [4, "2026-06-07", "Present"], [4, "2026-06-08", "Absent"], [4, "2026-06-09", "Absent"], [4, "2026-06-10", "Absent"],
    [5, "2026-06-01", "Present"], [5, "2026-06-02", "Present"], [5, "2026-06-03", "Present"], [5, "2026-06-04", "Present"], [5, "2026-06-05", "Present"],
    [5, "2026-06-06", "Absent"], [5, "2026-06-07", "Absent"], [5, "2026-06-08", "Absent"], [5, "2026-06-09", "Absent"], [5, "2026-06-10", "Absent"],
    [6, "2026-06-01", "Present"], [6, "2026-06-02", "Present"], [6, "2026-06-03", "Present"], [6, "2026-06-04", "Present"], [6, "2026-06-05", "Present"],
    [6, "2026-06-06", "Present"], [6, "2026-06-07", "Absent"], [6, "2026-06-08", "Absent"], [6, "2026-06-09", "Absent"], [6, "2026-06-10", "Absent"],
    [7, "2026-06-01", "Present"], [7, "2026-06-02", "Present"], [7, "2026-06-03", "Present"], [7, "2026-06-04", "Present"], [7, "2026-06-05", "Absent"],
    [7, "2026-06-06", "Absent"], [7, "2026-06-07", "Absent"], [7, "2026-06-08", "Absent"], [7, "2026-06-09", "Absent"], [7, "2026-06-10", "Absent"],
    [8, "2026-06-01", "Present"], [8, "2026-06-02", "Present"], [8, "2026-06-03", "Present"], [8, "2026-06-04", "Absent"], [8, "2026-06-05", "Absent"],
    [8, "2026-06-06", "Absent"], [8, "2026-06-07", "Absent"], [8, "2026-06-08", "Absent"], [8, "2026-06-09", "Absent"], [8, "2026-06-10", "Absent"],
    [9, "2026-06-01", "Present"], [9, "2026-06-02", "Present"], [9, "2026-06-03", "Absent"], [9, "2026-06-04", "Absent"], [9, "2026-06-05", "Absent"],
    [9, "2026-06-06", "Absent"], [9, "2026-06-07", "Absent"], [9, "2026-06-08", "Absent"], [9, "2026-06-09", "Absent"], [9, "2026-06-10", "Absent"],
    [10, "2026-06-01", "Present"], [10, "2026-06-02", "Absent"], [10, "2026-06-03", "Absent"], [10, "2026-06-04", "Absent"], [10, "2026-06-05", "Absent"],
    [10, "2026-06-06", "Absent"], [10, "2026-06-07", "Absent"], [10, "2026-06-08", "Absent"], [10, "2026-06-09", "Absent"], [10, "2026-06-10", "Absent"]
]
marks_data = [
    [1, "Python", 92], [1, "DBMS", 88], [1, "DSA", 91],
    [2, "Python", 75], [2, "DBMS", 81], [2, "DSA", 79],
    [3, "Python", 67], [3, "DBMS", 72], [3, "DSA", 70],
    [4, "Python", 95], [4, "DBMS", 90], [4, "DSA", 94],
    [5, "Python", 58], [5, "DBMS", 64], [5, "DSA", 61],
    [6, "Python", 84], [6, "DBMS", 87], [6, "DSA", 82],
    [7, "Python", 73], [7, "DBMS", 76], [7, "DSA", 71],
    [8, "Python", 89], [8, "DBMS", 92], [8, "DSA", 90],
    [9, "Python", 62], [9, "DBMS", 68], [9, "DSA", 65],
    [10, "Python", 98], [10, "DBMS", 96], [10, "DSA", 99]
]