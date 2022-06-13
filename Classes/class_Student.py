class Student():
    def __init__(self, firstname: str, lastname: str, gender: str, id: str, education: str, faculties: str, schedule: str):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.id = id
        self.education = education
        self.faculties = faculties
        self.schedule = schedule


    def set_firstname(self, newFirstname):
        """ændre fornavn"""
        self.firstname = newFirstname

    def set_lastname(self, newLastname):
        """ændre efternavn"""
        self.lastname = newLastname


    def get_fullname(self):
        """print fullname"""
        print(self.firstname + " " + self.lastname)

    def get_gender(self):
        """print køn"""
        print(self.gender)

    def get_id(self):
        """print id"""
        print(self.id)

    def get_education(self):
        """print uddannelsesnavn"""
        print(self.education)

    def set_faculties(self, newFaculty):
        """ændre fakultet"""
        self.faculties = newFaculty

    def get_faculties(self):
        """print fakultet"""
        print(self.faculties)

    def set_schedule(self, newSchedule):
        """ændre skemaet"""
        self.schedule = newSchedule

    def get_schedule(self):
        """print skema"""
        print(self.schedule)


