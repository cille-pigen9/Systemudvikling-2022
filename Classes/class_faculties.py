from class_address import*

class faculties():
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __get__name__(self, name):
        """print fakultet navn"""
        self.name = name

    def __get__id__(self, id):
        """print fakultet id"""
        self.id = id
