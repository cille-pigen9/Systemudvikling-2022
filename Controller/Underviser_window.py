import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt6 import uic
#from Controller import dbconnection
#from Controller.TeacherGUI import teacherwindowUI
#from Controller.AdminGUI import adminwindowUI
#from Controller.StudentGUI import studentwindowUI


class Underviser_window(QMainWindow):
    def __init__(self):
        super(Underviser_window, self).__init__()
        #Loader den specifikke Views fil
        uic.loadUi("../View/Skema_Und.ui",self)

        #Viser appen
        self.show()


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Underviser_window()
UIWindow.show()
app.exec()