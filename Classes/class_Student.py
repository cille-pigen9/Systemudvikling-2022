from class_address import*

class Student():
    def __init__(self, firstname: str, lastname: str, gender: str, id: int, education: str, faculties: str, schedule: str):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.id = id
        self.education = education
        self.faculties = faculties
        self.schedule = schedule


    def __set__firstname__(self, newFirstname):
        """ændre fornavn"""
        self.firstname = newFirstname

    def __set__lastname__(self, newLastname):
        """ændre efternavn"""
        self.lastname = newLastname

    def __get__fullname(self):
        """print fullname"""
        print(self.firstname + " " + self.lastname)

    def __get__gender__(self):
        """print køn"""
        print(self.gender)

    def __get__id__(self):
        """print id"""
        print(self.id)

    def __get__education__(self):
        """print uddannelsesnavn"""
        print(self.education)

    def __set__faculties__(self, newFaculty):
        """ændre fakultet"""
        self.faculties = newFaculty

    def __get__faculties__(self):
        """print fakultet"""
        print(self.faculties)

    def __set__schedule__(self, newSchedule):
        """ændre skemaet"""
        self.schedule = newSchedule

    def __get__schedule__(self):
        """print skema"""
        print(self.schedule)


