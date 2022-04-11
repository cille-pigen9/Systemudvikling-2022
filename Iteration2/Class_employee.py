class employee():
    def __init__(self, name: str, id: str, gender: str, adress: str, list_courses: []):
        self.name = name
        self.id = id
        self.gender = gender
        self.adress = adress
        self.list_courses = list_courses

    def __str__(self):
        return f"name:{self.name}, id: {self.id}, gender: {self.gender}, adress: {self.adress}, kurser: {self.list_courses}"
