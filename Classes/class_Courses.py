from class_address import*

class courses:
    def __init__(self, courseName, courseId, teacher, studentList, courseDate, classRoom):
        self.courseName = courseName
        self.courseId = courseId
        self.Teacher = teacher
        self.studentList = studentList
        self.courseDate = courseDate
        self.classRoom = classRoom

    def __get__courseName__(self):
        """Print course name"""
        print(self.courseName)

    def __get__courseId__(self):
        """Print course name"""
        print(self.courseId)


    def __set__teacher__(self, newTeacher):
        """Der kan komme nye undervisere, så disse skal kunne ændres"""
        self.teacher = newTeacher

    def __get__teacher__(self):
        "print teacher"
        print(self.teacher)

    def __set__studentList__(self, newStudentList):
        """tilføj studerende til listen"""
        self.studentList = newStudentList

    def __get__studentList(self):
        print(self.studentList)

    def __set__courseDate__(self, newCourseDate):
        """man skal kunne ændre kursus datoen"""
        self.courseDate = newCourseDate

    def __get__courseDate__(self):
        """print kursus dato"""
        print(self.courseDate)

    def __set__classRoom__(self, newClassRoom):
        """nyt klasselokale skal kunne ændres"""
        self.classRoom = newClassRoom

    def __get__classRoom__(self):
        """print klasselokale"""
        print(self.classRoom)

