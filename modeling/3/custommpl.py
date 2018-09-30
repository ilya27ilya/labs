#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import random
import math
from PyQt5.uic import loadUiType

Ui_MainWindow, QMainWindow = loadUiType('main_gui.ui')

def uniform_function(x, a, b):
    if x < a:
        return 0
    elif x >= a and x <= b:
        return (x - a) / (b - a)
    else:
        return 1


def uniform_density(x, a, b):
    if x >= a and x <= b:
        return 1 / (b - a)
    else:
        return 0


def normal_function(x, mu, sigm):
    return 0.5 * (1 + math.erf((x - mu) / math.sqrt(2 * sigm * sigm)))


def normal_density(x, mu, sigm):
    return 1 / (sigm * math.sqrt(2 * math.pi)) * math.exp(-(x - mu) * (x - mu) / (2 * sigm * sigm))


def get_normal_function_points(mu, sigm, x1, x2):
    if x2 < x1:
        x1, x2 = x2, x1
    x1 -= 1
    x2 += 1   
    delta = 0.01
    n = int((x2 - x1) / delta)
    
    x = x1
    y = normal_function(x, mu, sigm)
    x_points = list()
    y_points = list()
    for i in range(n):
        x_points.append(x)
        y_points.append(y)
        x += delta
        y = normal_function(x, mu, sigm)
    return x_points, y_points

def get_normal_density_points(mu, sigm, x1, x2):
    if x2 < x1:
        x1, x2 = x2, x1
    x1 -= 1
    x2 += 1   
    delta = 0.01
    n = int((x2 - x1) / delta)
    
    x = x1
    y = normal_density(x, mu, sigm)
    x_points = list()
    y_points = list()
    for i in range(n):
        x_points.append(x)
        y_points.append(y)
        x += delta
        y = normal_density(x, mu, sigm)
    return x_points, y_points


def get_uniform_function_points(a, b, x1, x2):
    if x2 < x1:
        x1, x2 = x2, x1
    x1 -= 1
    x2 += 1
    if b < a:
        a, b = b, a
    delta = 0.01
    n = int((x2 - x1) / delta)
    
    x = x1
    y = uniform_function(x, a, b)
    x_points = list()
    y_points = list()
    for i in range(n):
        x_points.append(x)
        y_points.append(y)
        x += delta
        y = uniform_function(x, a, b)
    return x_points, y_points

def get_uniform_density_points(a, b, x1, x2):
    if x2 < x1:
        x1, x2 = x2, x1
    x1 -= 1
    x2 += 1
    if b < a:
        a, b = b, a
    delta = 0.01
    n = int((x2 - x1) / delta)
    
    x = x1
    y = uniform_density(x, a, b)
    x_points = list()
    y_points = list()
    for i in range(n):
        x_points.append(x)
        y_points.append(y)
        x += delta
        y = uniform_density(x, a, b)
    return x_points, y_points

_translate = QtCore.QCoreApplication.translate


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.normal_choice.clicked.connect(self.change_plot)
        self.uniform_choice.clicked.connect(self.change_plot)
        self.run_button.clicked.connect(self.run_plot)
        self.plot = 0;
        self.fig = Figure()
        self.ax1f1 = self.fig.add_subplot(111)
        self.ax1f2 = self.fig.add_subplot(111)
        self.addmpl(self.fig)

    def run_plot(self):
        if self.plot == 0:
            a = float(str(self.first_param_edit.text()).replace(',','.'))
            b = float(str(self.second_param_edit.text()).replace(',','.'))
            mx = (a + b) / 2
            dx = (b - a) ** 2 / 12
            self.mx_value_label.setText(_translate("mplfigs", str(mx)))
            self.dx_value_label.setText(_translate("mplfigs", str(dx)))
            x1 = float(str(self.x1_edit.text()).replace(',','.'))
            x2 = float(str(self.x2_edit.text()).replace(',','.'))
            x_points, y_points = get_uniform_function_points(a, b, x1, x2)
            self.ax1f1.clear()
            self.ax1f2.clear()
            self.ax1f1.plot(x_points, y_points)
            self.canvas.draw()
            x_points, y_points = get_uniform_density_points(a, b, x1, x2)
            self.ax1f2.plot(x_points, y_points)
            self.canvas.draw()

        else:
            mu = float(str(self.first_param_edit.text()).replace(',','.'))
            sigm = float(str(self.second_param_edit.text()).replace(',','.'))
            mx = mu
            dx = sigm ** 2
            self.mx_value_label.setText(_translate("mplfigs", str(mx)))
            self.dx_value_label.setText(_translate("mplfigs", str(dx)))
            x1 = float(str(self.x1_edit.text()).replace(',','.'))
            x2 = float(str(self.x2_edit.text()).replace(',','.'))
            self.ax1f1.clear()
            self.ax1f2.clear()
            x_points, y_points = get_normal_function_points(mu, sigm, x1, x2)
            self.ax1f1.plot(x_points, y_points)
            x_points, y_points = get_normal_density_points(mu, sigm, x1, x2)
            self.ax1f2.plot(x_points, y_points)
            self.canvas.draw()

    def change_plot(self):
        if self.plot == 0:
            self.first_param_label.setText(_translate("mplfigs", "mu = "))
            self.second_param_label.setText(_translate("mplfigs", "sigma = "))
            self.plot = 1
        else:
            self.first_param_label.setText(_translate("mplfigs", "A = "))
            self.second_param_label.setText(_translate("mplfigs", "B = "))
            self.plot = 0

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw() 

if __name__ == '__main__':
    import sys
    from PyQt5 import QtGui
    import PyQt5
    import numpy as np
 
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
