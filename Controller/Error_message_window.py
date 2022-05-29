import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt6 import uic
#from Controller import dbconnection
#from Controller.TeacherGUI import teacherwindowUI
#from Controller.AdminGUI import adminwindowUI
#from Controller.StudentGUI import studentwindowUI


class Error_message_window(QMainWindow):
    def __init__(self):
        super(Error_message_window, self).__init__()
        #Loader den specifikke Views fil
        uic.loadUi("../View/Error_message.ui",self)

        #Viser appen
        self.show()


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Error_message_window()
UIWindow.show()
app.exec()