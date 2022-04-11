class courses:
    def __init__(self, course_name, course_id, employee, course_date, adress, class_room):
        self.course_name = course_name
        self.course_id = course_id
        self.employee = employee
        self.course_date = course_date
        self.adress = adress
        self.class_room = class_room
    def __str__(self):
        return f"name: {self.course_name}, id: {self.course_id}, employee: {self.employee}/" \
               f"date: {self.course_date},adress: {self.adress}, class_room: {self.class_room}"