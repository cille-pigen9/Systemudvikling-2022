from lxml import etree, objectify
from io import BytesIO
from Classes.class_course import course
from Elements import Elements


class CoursesToXml:
    def __init__(self, Course: course):
        self.course = Course

    def write_file(self):

        root = etree.Element("courses")
        for courses in self.course.get_course():
            course_element = Elements.create_course(courses)
            root.append(course_element)

            studentList = objectify.SubElement(course_element, "studentList")

            for Student in courses.get_Student():
                student_element = Elements.create_student(Student)
                studentList.append(student_element)

        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        parser = etree.XMLParser(remove_blank_text=True)
        file_obj = BytesIO(etree.tostring(root))
        tree = etree.parse(file_obj, parser)

        try:
            with open("courses.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding="utf-8", xml_declaration=True)
        except IOError:
            pass
