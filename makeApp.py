import re
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
)
from PyQt5 import QtGui

from models.MainModel import MainModel
from views.MainView import MainView
from controllers.MainController import MainController


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("makeApp Generador de Código")
        self.resize(800,600)
        self.move(500,100)
        self.setWindowIcon(QtGui.QIcon('assets/images/icono.png'))

        # create a model
        self.__modelo = MainModel()

        # create a view and place it on the root window
        self.__vista = MainView(self) # Set the layout on the application's window
        self.setLayout(self.__vista.layout())
        
                
        # create a controller
        self.__controlador = MainController(self.__modelo, self.__vista)

        # set the controller to view
        self.__vista.setController(self.__controlador)   
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
