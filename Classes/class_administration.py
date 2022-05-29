from class_address import address

class administration():
    def __init__(self, firstname: str, lastname: str, id: str, gender: str, schedule: str):
            self.firstname = firstname
            self.lastname = lastname
            self.id = id
            self.gender = gender
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

    def __get__id__(self):
        """print id"""
        print(self.id)

    def __get__gender__(self):
        """print køn"""
        print(self.gender)

    def __set__schedule__(self, newSchedule):
        """course changes"""
        self.schedule = newSchedule