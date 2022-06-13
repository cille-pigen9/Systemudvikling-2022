class courses:
    def __init__(self, courseName, courseId, teacher, Student, courseDate, classRoom):
        self.courseName = courseName
        self.courseId = courseId
        self.teacher = teacher
        self.Student = Student
        self.courseDate = courseDate
        self.classRoom = classRoom

    def get_courseName(self):
        """Print course name"""
        print(self.courseName)

    def get_courseId(self):
        """Print course name"""
        print(self.courseId)

    def set_teacher(self, newTeacher):
        """Der kan komme nye undervisere, så disse skal kunne ændres"""
        self.teacher = newTeacher

    def get_teacher(self):
        "print teacher"
        print(self.teacher)

    def set_Student(self, newStudent):
        """tilføj studerende til listen"""
        self.student = newStudent

    def get_Student(self):
        print(self.Student)

    def set_courseDate(self, newCourseDate):
        """man skal kunne ændre kursus datoen"""
        self.courseDate = newCourseDate

    def get_courseDate(self):
        """print kursus dato"""
        print(self.courseDate)

    def set_classRoom(self, newClassRoom):
        """nyt klasselokale skal kunne ændres"""
        self.classRoom = newClassRoom

    def get_classRoom(self):
        """print klasselokale"""
        print(self.classRoom)

