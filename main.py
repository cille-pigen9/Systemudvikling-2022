from lxml import etree, objectify

from dummyObject import dummyObjects
from coursesToXml import CoursesToXml
from XmlToCourses import XmlToCourses

if __name__ == "__main":
    print("lav til test objekts")
    courseList = dummyObjects.create()
    print("skirv courseList to course.xml")
    CoursesToXml(courseList).write_file()

    print("læs xml filen")

    courseList = XmlToCourses('course.xml').parseXML()

    print("courseList er af typen:", type(courseList))

    course = courseList.get_course()
    print("course er a typen:", type(course))
    print(course)
    print("iterating over the objects and printing them:")

    for c in course:
        print("-" * 30)
        print()
        print("course:", c.get_courseName(), c.get_courseId(), c.get_teacher(), c.get_studentList(), c.get_courseDate(), c.get_classRoom())
        print("list of students:")
        for s in c.get_studentList():
            print("\t", s.get_fullname(), ",", s.get_gender(), ",", s.get_id(), ",", s.get_faculties(), ",", s.get_schedule())

    print("\nCecking documnets:\n")

    dtd = etree.DTD(open('courses.dtd'))
    print("check generated course.xml", dtd.validate(etree.parse('course.xml')))
    print("check invalid courses_invalid.xml", dtd.validate(etree.parse('courses_invalid.xml')))