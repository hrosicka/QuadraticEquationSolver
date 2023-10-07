import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QGroupBox,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QGridLayout,
    QMenuBar,
    QMenu,
    QAction,
)

from PyQt5.QtGui import (
    QDoubleValidator,
    QFont,
    QIntValidator,
    QPixmap,
)
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


        self.setWindowTitle('Quadratic Equation')

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
        
        validator = QIntValidator(-10000, 1000, self)

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
        self.edit_a.setValidator(validator)
        self.layout_coef.addWidget(self.edit_a,1,1)
        

        self.label_b = QLabel("b:")
        self.label_b.setAlignment(QtCore.Qt.AlignLeft)
        self.layout_coef.addWidget(self.label_b,1,2)

        self.edit_b = QLineEdit(self)
        self.edit_b.setAlignment(QtCore.Qt.AlignRight)
        self.edit_b.setToolTip("Enter coefficent b")
        self.edit_b.setValidator(validator)
        self.layout_coef.addWidget(self.edit_b,1,3)

        self.label_c = QLabel("c:")
        self.label_c.setAlignment(QtCore.Qt.AlignLeft)
        self.layout_coef.addWidget(self.label_c,1,4)

        self.edit_c = QLineEdit(self)
        self.edit_c.setAlignment(QtCore.Qt.AlignRight)
        self.edit_c.setToolTip("Enter coefficent c")
        self.edit_c.setValidator(validator)
        self.layout_coef.addWidget(self.edit_c,1,5)

  
    def layoutEquation(self):

        self.layout_equation = QGridLayout()

        self.label_equation = QLabel("")
        self.label_equation.setFont(QFont('Sans Serif', 10))
        self.label_equation.setAlignment(QtCore.Qt.AlignLeft)
        self.layout_equation.addWidget(self.label_equation,0,0,1,6)

        

    def solve(self):
        self.display()




    def display(self):

        coeff_a = self.edit_a.text()
        coeff_b = self.edit_b.text()
        coeff_c = self.edit_c.text()

        try:
            a = int(coeff_a)
            b = int(coeff_b)
            c = int(coeff_c)

            self.edit_a.setStyleSheet("background-color : white; color : black")
            self.edit_b.setStyleSheet("background-color : white; color : black")
            self.edit_c.setStyleSheet("background-color : white; color : black")

            try:
                res = 1 / a

                self.edit_a.setStyleSheet("background-color : white; color : black")
                self.edit_b.setStyleSheet("background-color : white; color : black")
                self.edit_c.setStyleSheet("background-color : white; color : black")

            except Exception:
                self.edit_a.setStyleSheet("background-color : pink; color : black")
                QMessageBox.about(self, 'Error','Coefficient a cannot be zero')

            else:
                self.label_equation.setText(self.display_equation_format(a, b, c))

        except Exception:
            self.edit_a.setStyleSheet("background-color : pink; color : black")
            self.edit_b.setStyleSheet("background-color : pink; color : black")
            self.edit_c.setStyleSheet("background-color : pink; color : black")
            QMessageBox.about(self, 'Error','Input can only be an integer')

        

    def display_equation_format(self, a, b, c):
        """
        Assembly quadratic equation

        a - coefficient a - int

        b - coefficient b - int

        c - coefficient c - int

        return string (example 5x<sup>2</sup>+5x+5)
        """
        equation = self.first_term(a) + self.second_term(b) + self.third_term(c) + "=0"
        return equation
        

    def first_term(self, a):
        """
        First quadratic term in quadratic equation

        a - coefficient a - int

        return string (example 5x<sup>2</sup> )
        """
        if a == 1:
            a = "x<sup>2</sup>"
        elif a == -1:
            a = "-x<sup>2</sup>"
        else:
            a = str(a) + "x<sup>2</sup>"

        return a


    def second_term(self, b):
        """
        Second linear term in quadratic equation

        b - coefficient b - int
        
        return string (example 5x )
        """
        if b == 1:
            b = "+x"
        elif b == -1:
            b = "-x"
        elif b > 0:
            b = "+" + str(b) + "x"
        elif b == 0:
            b = ""
        else:
            b = str(b) + "x"

        return b
    
    def third_term(self, c):
        """
        Third constant term in quadratic equation

        c - coefficient c - int
        
        return string (example 5)
        """
        if c > 0:
            c = "+" + str(c)
        elif c == 0:
            c = ""
        else:
            c = str(c)

        return c
   
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()