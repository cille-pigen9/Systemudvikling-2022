import unittest
from class_Courses import*
class testCourses(unittest.TestCase):

    newCourse = courses("systemudvikling", "5100", "Hugo", "Cecilie", "29/5-2022", "401")

    print(newCourse.get_courseName())

    newCourse.set_courseDate("26/6-2022")
    print(newCourse.get_courseDate())

