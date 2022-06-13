from lxml import etree, objectify
from io import BytesIO
import Classes.class_Courses as class_Courses
from Elements import Elements

class CoursesToXml:
    def __init__(self, courses: class_Courses):
        self.courses = courses

    def write_file(self):

        root = etree.Element("courses")
        for courseName in self.courses.__get__courseName__():
            course_element = Elements.create_course(courseName)
            root.append(course_element)

            studentList = objectify.SubElement(course_element, "studentList")
            studentList_element = Elements.create_studentlist(studentList)
            studentList.append(studentList_element)

        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        parser = etree.XMLParser(remove_blank_text=True)
        file_obj = BytesIO(etree.tostring(root))
        tree = etree.parse(file_obj, parser)

        try:
            with open("courses.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding = "utf-8", xml_declaration=True)
        except IOError:
            pass