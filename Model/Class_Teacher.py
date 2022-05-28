class Teacher():
    def __init__(self, firstname: str, lastname:str, id: str, gender: str, schedule, faculties, list_courses: []):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.gender = gender
        self.schedule = schedule
        self.faculties = faculties
        self.list_courses = list_courses

    def __str__(self):
        return f"firstname:{self.firstname}, lastname:{self.lastname}, id: {self.id}, gender: {self.gender} " \
               f"schedule:{self.schedule}, faculties:{self.faculties}, kurser: {self.list_courses}"
