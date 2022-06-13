from lxml import objectify
from Classes.class_Student import Student
from Classes.class_Courses import courses


class Elements:
    @staticmethod
    def create_student(student_obj: Student):
        Student = objectify.Element("Student")
        Student.fullname = student_obj.get_fullname()
        Student.gender = student_obj.get_gender()
        Student.id = student_obj.get_id()
        Student.education = student_obj.get_education()
        Student.faculties = student_obj.get_faculties()
        Student.schedule = student_obj.get_schedule()
        return Student

    @staticmethod
    def create_course(course_obj: courses):
        courses = objectify.Element("courses")
        courses.courseName = course_obj.get_courseName()
        courses.courseId = course_obj.get_courseId()
        courses.teacher = course_obj.get_teacher()
        courses.studentList = course_obj.get_Student()
        courses.courseDate = course_obj.get_courseDate()
        courses.classRoom = course_obj.get_classRoom()
        return courses
