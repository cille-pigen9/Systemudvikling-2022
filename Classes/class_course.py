
from Classes.class_Courses import courses

class course:
    def __init__(self):
        self.course = []

    def append_courses(self, courses = courses):
        self.course.append(courses)

    def get_course(self):
        return self.course
