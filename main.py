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


from matplotlib import pyplot as plt

import numpy as np

import quadratic_equation

import canvas


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.sc = canvas.MplCanvas(self, width=6, height=6, dpi=100)

        self.setWindowTitle('Quadratic Equation')

        self.setMinimumWidth(600)
        self.setMinimumHeight(300)

        self.setMaximumWidth(1200)
        self.setMaximumHeight(600)

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
        self.layoutSolution()

        groupBoxCoef = QGroupBox("Coefficients")
        groupBoxCoef.setLayout(self.layout_coef)


        groupBoxEquation = QGroupBox("Quadratic equation")
        groupBoxEquation.setLayout(self.layout_equation)

        groupBoxSolution = QGroupBox("Solution")
        groupBoxSolution.setLayout(self.layout_solution)


        verticalLayout.addWidget(groupBoxCoef)
        verticalLayout.addWidget(groupBoxEquation)
        verticalLayout.addWidget(groupBoxSolution, 1)
 
        

        mainHorizontalLayout = QHBoxLayout()
        mainHorizontalLayout.addLayout(verticalLayout)
        mainHorizontalLayout.addWidget(self.sc)

        outerVerticalLayout = QVBoxLayout()
        outerVerticalLayout.addLayout(mainHorizontalLayout)
        outerVerticalLayout.addStretch(1)
        outerVerticalLayout.addLayout(horizontalLayout)
        

        w = QWidget()
        w.setLayout(outerVerticalLayout)
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
        self.label_equation.setAlignment(QtCore.Qt.AlignCenter)
        self.layout_equation.addWidget(self.label_equation,0,0,1,6)


    def layoutSolution(self):

        self.layout_solution = QGridLayout()

        self.label_three_type_solution = QLabel('Type of solution')
        self.layout_solution.addWidget(self.label_three_type_solution,0,0,1,6)

        self.label_discriminant = QLabel('Discriminant D:')
        self.layout_solution.addWidget(self.label_discriminant,1,0)

        self.label_discriminant_number = QLabel('')
        self.layout_solution.addWidget(self.label_discriminant_number,1,1,1,5)

        self.label_x1_root = QLabel('Root x1:')
        self.layout_solution.addWidget(self.label_x1_root,2,0)

        self.label_x1_root_number = QLabel('')
        self.label_x1_root_number.setFont(QFont('Sans Serif', 10))
        self.layout_solution.addWidget(self.label_x1_root_number,2,1,1,5)

        self.label_x2_root = QLabel('Root x2:')
        self.layout_solution.addWidget(self.label_x2_root,3,0)

        self.label_x2_root_number = QLabel('')
        self.label_x2_root_number.setFont(QFont('Sans Serif', 10))
        self.layout_solution.addWidget(self.label_x2_root_number,3,1,1,5)

        self.label_vertex = QLabel('Vertex:')
        self.layout_solution.addWidget(self.label_vertex,4,0)

        self.label_vertex_number = QLabel('')
        self.label_vertex_number.setFont(QFont('Sans Serif', 10))
        self.layout_solution.addWidget(self.label_vertex_number,4,1,1,5)


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

                qe = quadratic_equation.QuadraticEquation(a, b, c)
                self.discriminant = qe.discriminant()
                self.label_three_type_solution.setText(qe.equation_type(self.discriminant))
                self.label_discriminant_number.setText(str(self.discriminant))
                qe.solve()
                self.x1_root = qe.x1
                self.x2_root = qe.x2
                self.label_x1_root_number.setText(str(self.x1_root))
                self.label_x2_root_number.setText(str(self.x2_root))
                self.vertex_x = qe.vertex_x
                self.vertex_y = qe.vertex_y
                self.label_vertex_number.setText('('+str(self.vertex_x)+', '+str(self.vertex_y)+')')

                self.sc.axes.cla()
                x = np.linspace(self.vertex_x-10, self.vertex_x+10, 1000)
                y = a * x ** 2 + b * x + c
                self.sc.axes.plot(x, y)
                self.sc.axes.plot(self.vertex_x, self.vertex_y, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="blue")
                self.sc.draw()

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