class faculties():
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __str__(self):
        return f" name: {self.name}, id: {self.id}"

