import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt6 import uic
#from Controller import dbconnection
#from Controller.TeacherGUI import teacherwindowUI
#from Controller.AdminGUI import adminwindowUI
#from Controller.StudentGUI import studentwindowUI


class Studerende_window(QMainWindow):
    def __init__(self):
        super(Studerende_window, self).__init__()
        #Loader den specifikke Views fil
        uic.loadUi("../View/Skema_Stu.ui",self)



        #Viser appen
        self.show()


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Studerende_window()
UIWindow.show()
app.exec()