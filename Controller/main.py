import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt6 import uic
#from Controller import dbconnection
#from Controller.TeacherGUI import teacherwindowUI
#from Controller.AdminGUI import adminwindowUI
#from Controller.StudentGUI import studentwindowUI


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        #Loader den specifikke Views fil
        uic.loadUi("../View/login.ui",self)

        #Definerer Views filens widgets
        self.lineEdit_username = self.findChild(QLineEdit, "lineEdit_username")
        self.lineEdit_password = self.findChild(QLineEdit, "lineEdit_password")
        self.pushButton_Login = self.findChild(QPushButton, "pushButton_Login")
        #self.GlemtLoginButton = self.findChild(QPushButton, "GlemtLoginButton")

        #Hvad widgets skal gøre
        self.pushButton_Login.clicked.connect(self.loginfunction)
        #self.Password.returnPressed.connect(self.loginfunction)

        #Viser appen
        self.show()

    def loginfunction(self):
        lineEdit_username = self.lineEdit_username.text()
        lineEdit_password = self.lineEdit_password.text()
        print(lineEdit_username, lineEdit_password)


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Login()
UIWindow.show()
app.exec()