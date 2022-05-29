import unittest
from class_Courses import*
class testCourses(unittest.TestCase):

    newCourse = courses("systemudvikling", "5100", "Hugo", "Cecilie", "29/5-2022", "401")

    print(newCourse.__get__courseName__())

    newCourse.__set__courseDate__("26/6-2022")
    print(newCourse.__get__courseDate__())

