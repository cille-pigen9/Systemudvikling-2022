import os
from xml.etree import ElementTree
from class_Courses import courses

class courseReader:
    __file__name__ = "courses.xml"

    def __init__(self) -> None:
        full_file = os.path.abspath(os.path.join("data", self.__file__name__))
        dom = ElementTree.parse(full_file)

        root = dom.getroot()
        courseName = root.attrib["courseName"]
        courseId = root.attrib["courseId"]
        teacher = root.attrib["teacher"]
        studentList = root.attrib["studentList"]
        courseDate = root.attrib["courseDate"]
        classRoom = root.attrib["classRoom"]

        print("change course date", courseDate)

        self.__courses__= courses(courseName, courseId, teacher, studentList, courseDate, classRoom)

        def getCourses(self) -> courses:
            return self.__courses__



