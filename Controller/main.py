import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt6 import uic
from Controller import Database_connection
#from Controller.Underviser_window import Underviser_window
#from Controller.Sekretaer_window import Sekretaer_window
#from Controller.Studerende_window import Studerende_window
#from Controller.Error_message_window import Error_message_window


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        #Loader View filen
        uic.loadUi("../View/login.ui",self)

        #View filens widgets bliver defineret
        self.lineEdit_username = self.findChild(QLineEdit, "lineEdit_username")
        self.lineEdit_password = self.findChild(QLineEdit, "lineEdit_password")
        self.pushButton_Login = self.findChild(QPushButton, "pushButton_Login")
        #self.forgot_password = self.findChild(QLabel, "forgot_password")

        #Funktionen af widgets
        self.pushButton_Login.clicked.connect(self.loginfunction)
        #self.Password.returnPressed.connect(self.loginfunction)

        #Fremvisning af appen
        self.show()

    def loginfunction(self):
        lineEdit_username = self.lineEdit_username.text()
        lineEdit_password = self.lineEdit_password.text()

        brugerlogin = Database_connection.check_password(lineEdit_username, lineEdit_password)
        print(brugerlogin)
        dbcon = Database_connection.get_connection()
        mycursor = dbcon.cursor()
        query = "SELECT user.iduser, student.idstudent FROM 206001.user JOIN 206001.student WHERE user.userName = %s"
        mycursor.execute(query, brugerlogin[2])
        results = mycursor.fetchall()
        user = []
        for result in results:
            user.append(result[0], result[1])
        if brugerlogin[0] == True and brugerlogin[1] == user[1]:
            self.close()
            self.Studerende_window.show()



#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Login()
UIWindow.show()
app.exec()