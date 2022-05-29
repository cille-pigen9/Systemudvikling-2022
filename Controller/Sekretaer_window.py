import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt6 import uic
#from Controller import dbconnection
#from Controller.TeacherGUI import teacherwindowUI
#from Controller.AdminGUI import adminwindowUI
#from Controller.StudentGUI import studentwindowUI


class Sekretaer_window(QMainWindow):
    def __init__(self):
        super(Sekretaer_window, self).__init__()
        #Loader den specifikke Views fil
        uic.loadUi("../View/Sek_Skema_1.ui",self)

        #Viser appen
        self.show()


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Sekretaer_window()
UIWindow.show()
app.exec()