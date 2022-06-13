from Classes.class_Student import Student
from Classes.class_Courses import courses
from Classes.class_course import course

class dummyObjects:

    @staticmethod
    def create():
        studentList1 = []
        studentList2 = []
        student1 = Student("Ditte", "Knudsen", "Female", "hfj432", "Sundhed og informatik", "farma", "Skema")
        studentList1.append(student1)
        student2 = Student("Cille", "Ludvigsen", "Female", "fhd433", "Sundhed og informatik" "DTU", "Skema")
        studentList1.append(student2)
        student3 =  Student("Kerim", "Gumus", "Male", "asw234", "Science", "Sundhed og informatik", "Skema")
        studentList2.append(student3)
        student4 = Student("Sadek", "Al-Taai", "Male", "olk234", "Sundhed og informatik", "Farma", "Skema")
        studentList2.append(student4)

        courseA = courses("Systemudvikling", "5100-B3-4F22", "Hugo", studentList1, "13/06-2022", "bi - 2-1-07/09")
        courseB = courses("Sygdomslære for ikke-klinikkere", "3930-4F22", "Mette", studentList2, "26/06-2022", "Panum - 31-01-60a")
        courseList = course()
        courseList.append_courses(courseA)
        courseList.append_courses(courseB)

        return courseList

