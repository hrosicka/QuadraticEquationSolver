import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QGroupBox,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QGridLayout,
    QMenuBar,
    QMenu,
    QAction,
)

from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import numpy as np


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)




class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        self.setWindowTitle('PyQt Math App')

        self.setMinimumWidth(400)
        self.setMinimumHeight(400)

        self.setMaximumWidth(800)
        self.setMaximumHeight(800)

        buttonSolve = QPushButton('Solve')
        buttonSolve.clicked.connect(lambda: self.solve())

        buttonClose = QPushButton('Close')
        buttonClose.clicked.connect(self.close)

        horizontalLayout = QHBoxLayout()
        horizontalLayout.addStretch(1)
        horizontalLayout.addWidget(buttonSolve)
        horizontalLayout.addWidget(buttonClose)

        verticalLayout = QVBoxLayout()
        
        self.layoutCoef()
        self.layoutEquation()

        groupBoxCoef = QGroupBox("Coefficients")
        groupBoxCoef.setLayout(self.layout_coef)


        groupBoxEquation = QGroupBox("Quadratic equation")
        groupBoxEquation.setLayout(self.layout_equation)


        verticalLayout.addWidget(groupBoxCoef)
        verticalLayout.addWidget(groupBoxEquation)
        verticalLayout.addStretch(1)
        verticalLayout.addLayout(horizontalLayout)


        
        w = QWidget()
        w.setLayout(verticalLayout)
        self.setCentralWidget(w)


    def layoutCoef(self):

        self.layout_coef = QGridLayout()

        self.label_description = QLabel("Quadratic equation: ax<sup>2</sup>+bx+c=0")
        self.label_description.setAlignment(QtCore.Qt.AlignLeft)
        self.layout_coef.addWidget(self.label_description,0,0,1,6)

        self.label_a = QLabel("a:")
        self.label_a.setAlignment(QtCore.Qt.AlignLeft)
        self.layout_coef.addWidget(self.label_a,1,0)

        self.edit_a = QLineEdit(self)
        self.edit_a.setAlignment(QtCore.Qt.AlignRight)
        self.edit_a.setToolTip("Enter coefficent a ≠ 0")
        self.layout_coef.addWidget(self.edit_a,1,1)
        

        self.label_b = QLabel("b:")
        self.label_b.setAlignment(QtCore.Qt.AlignLeft)
        self.layout_coef.addWidget(self.label_b,1,2)

        self.edit_b = QLineEdit(self)
        self.edit_b.setAlignment(QtCore.Qt.AlignRight)
        self.edit_b.setToolTip("Enter coefficent b")
        self.layout_coef.addWidget(self.edit_b,1,3)

        self.label_c = QLabel("c:")
        self.label_c.setAlignment(QtCore.Qt.AlignLeft)
        self.layout_coef.addWidget(self.label_c,1,4)

        self.edit_c = QLineEdit(self)
        self.edit_c.setAlignment(QtCore.Qt.AlignRight)
        self.edit_c.setToolTip("Enter coefficent c")
        self.layout_coef.addWidget(self.edit_c,1,5)

  
    def layoutEquation(self):

        self.layout_equation = QGridLayout()

        self.label_equation = QLabel("")
        self.label_equation.setAlignment(QtCore.Qt.AlignLeft)
        self.layout_equation.addWidget(self.label_equation,0,0,1,6)

        

    def solve(self):
        coeff_a = self.edit_a.text()
        
        coeff_b = int(self.edit_b.text())
        if coeff_b > 0:
            coeff_b = "+" + str(coeff_b)
        elif coeff_b == 0:
            coeff_b = ""
        else:
            coeff_b = str(coeff_b)

        coeff_c = int(self.edit_c.text())
        if coeff_c > 0:
            coeff_c = "+" + str(coeff_c)
        elif coeff_c == 0:
            coeff_c = ""
        else:
            coeff_c = str(coeff_c)


        self.label_equation.setText(coeff_a + "x<sup>2</sup> " + coeff_b + "x " + coeff_c + " = 0")
   

    
   
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()