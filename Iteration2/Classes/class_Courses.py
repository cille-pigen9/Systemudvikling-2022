class courses:
    def __init__(self, course_name, course_id, Teacher, course_date, address, class_room):
        self.course_name = course_name
        self.course_id = course_id
        self.Teacher = Teacher
        self.course_date = course_date
        self.address = address
        self.class_room = class_room

    def __str__(self):
        return f"name: {self.course_name}, id: {self.course_id}, employee: {self.Teacher}/" \
               f"date: {self.course_date},address: {self.address}, class_room: {self.class_room}"

