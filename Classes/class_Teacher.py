from class_address import*

class Teacher():
    def __init__(self, firstname: str, lastname:str, id: str, gender: str, schedule, faculties, courseList: []):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.gender = gender
        self.schedule = schedule
        self.faculties = faculties
        self.courseList = courseList

    def __set_lastname__(self, new_lastName):
        """hvis man bliver gift kan man skifte navn"""
        self.lastname = new_lastName

    def __get__fullname__(self):
        """print fullname"""
        print(self.firstname + " " + self.lastname)

    def __get__id__(self):
        print(self.id)

    def __get__gender__(self):
        print(self.gender)

    def __set__faculties__(self, newFaculties):
        self.faculties = newFaculties

    def __get__faculties__(self):
        print(self.faculties)

    def __set__scheduleRequest__(self, daysAvailable):
        self.schedule = daysAvailable

    def __get__schedule__(self):
        print(self.schedule)





teacher1 = Teacher("Leif", "Helbig", "25", "Epic", "Morning", "Diku", ["Sys", "Co"])

print(teacher1.firstname)


