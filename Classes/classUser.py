class user:
    def __init__(self):
        self.data = {}

    def createNewUser(self, userName, password):
        if login in self.data:
            raise AssertionError('User already exists')

        self.data[userName] = password

    def checkUsername(self, userName, password):
        if not userName in self.data:
            return False

        if self.data[userName] != password:
            return False

        return True