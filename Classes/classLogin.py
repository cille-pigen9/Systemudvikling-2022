
class login:
    def __init__(self):
        self.user = loginUser()

    def usernameAndPassword(self):
        username = input("username: ")
        password = input("password: ")
        return username, password

    def verificerUser(self):
        username, password  = self.usernameAndPassword()

        while not self.user.check_user(username, password):
            print("Wrong username or password")
            if input("Are you a new user?") == "y":
                print("Starting registration process")
                username, password = self.usernameAndPassword()
                self.user.addUser(username, password)
                print("Done. Try to login.")
            username, password = self.usernameAndPassword()

manager = login()
manager.verificerUser()