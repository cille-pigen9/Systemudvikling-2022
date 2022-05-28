class Administration():
    def __init__(self, Firstname: str, Lastname: str, id: str, gender: str):
            self.Firstname = Firstname
            self.Lastname = Lastname
            self.id = id
            self.gender = gender

    def __str__(self):
        return f"Firstname:{self.Firstname}, Lastname: {self.Lastname}, id: {self.id}, " \
               f"gender: {self.gender}"
