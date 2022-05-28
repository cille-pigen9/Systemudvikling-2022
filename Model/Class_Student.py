class Student():
    def __init__(self, Firstname: str, Lastname: str, age: int, gender: str, id: int, Education: str, Faculties: str, schedule: str):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.age = age
        self.gender = gender
        self.id = id
        self.Education = Education
        self.Faculties = Faculties
        self.schedule = schedule

    def __str__(self):
        return f"Firstname:{self.Firstname}, Lastname: {self.Lastname}, age: {self.age}, gender: {self.gender}"