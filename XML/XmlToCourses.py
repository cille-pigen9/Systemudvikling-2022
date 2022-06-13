from lxml import objectify
from Classes.class_Student import Student
from Classes.class_course import course
from Classes.class_Courses import courses

class XmlToCourses:

    def __init__(self, xml_filename):
        self.xml_filename = xml_filename

    def parseXML(self) -> course:
        with open(self.xml_filename, "rb") as f:
            xml = f.read()
        root = objectify.fromstring(xml)

        aattrib = root.attrib

        courseList = course()

        for courses in root.getchildren():
            students: [Student] = []
            for studentList in courses.studerende.getchildren():
                fornavn = studentList.fornavn.text
                print(fornavn)
                efternavn = studentList.efternavn.text
                print(efternavn)
                koen = studentList.koen.text
                print(koen)
                id = studentList.id.text
                print(id)
                uddannelse = studentList.uddannelse.text
                print(uddannelse)
                fakultet = studentList.fakultet.text
                print(fakultet)
                skema = studentList.skema.text
                print(skema)
                student = Student(fornavn, efternavn, koen, id, uddannelse, fakultet, skema)
                students.append(student)
            course_obj = courses(courses.kursusnavn, courses.kursusid, courses.lærer, students, courses.dato, courses.klassevarelse)
            courseList.append_courses(course_obj)
        return courseList
