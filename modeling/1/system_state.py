#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy

matrix = numpy.matrix
solve = numpy.linalg.solve


class Ui_window_form(object):
    def setupUi(self, window_form):
        window_form.setObjectName("window_form")
        window_form.resize(260, 370)
        window_form.setMinimumSize(QtCore.QSize(260, 370))
        window_form.setMaximumSize(QtCore.QSize(260, 370))
        self.gridLayout = QtWidgets.QGridLayout(window_form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.state_count_label = QtWidgets.QLabel(window_form)
        self.state_count_label.setObjectName("state_count_label")
        self.horizontalLayout.addWidget(self.state_count_label)
        self.state_count_spinbox = QtWidgets.QSpinBox(window_form)
        self.state_count_spinbox.setMinimum(2)
        self.state_count_spinbox.setMaximum(10)
        self.state_count_spinbox.setProperty("value", 5)
        self.state_count_spinbox.setObjectName("state_count_spinbox")
        self.horizontalLayout.addWidget(self.state_count_spinbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_table = QtWidgets.QTableWidget(window_form)
        self.input_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.input_table.setRowCount(5)
        self.input_table.setColumnCount(5)
        self.input_table.setObjectName("input_table")
        self.input_table.horizontalHeader().setDefaultSectionSize(40)
        self.input_table.horizontalHeader().setMinimumSectionSize(40)
        self.input_table.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout.addWidget(self.input_table)
        self.run_button = QtWidgets.QPushButton(window_form)
        self.run_button.setObjectName("run_button")
        self.verticalLayout.addWidget(self.run_button)
        self.average_time_label = QtWidgets.QLabel(window_form)
        self.average_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.average_time_label.setObjectName("average_time_label")
        self.verticalLayout.addWidget(self.average_time_label)
        self.output_table = QtWidgets.QTableWidget(window_form)
        self.output_table.setMaximumSize(QtCore.QSize(16777215, 60))
        self.output_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.output_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.output_table.setRowCount(1)
        self.output_table.setColumnCount(5)
        self.output_table.setObjectName("output_table")
        self.output_table.horizontalHeader().setVisible(True)
        self.output_table.horizontalHeader().setDefaultSectionSize(40)
        self.output_table.horizontalHeader().setMinimumSectionSize(40)
        self.output_table.verticalHeader().setVisible(False)
        self.output_table.verticalHeader().setDefaultSectionSize(40)
        self.output_table.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout.addWidget(self.output_table)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.state_count_spinbox.valueChanged.connect(self.tables_init)
        self.run_button.clicked.connect(self.calculate)
        self.input_table_zero()
        self.output_table_zero()

        self.retranslateUi(window_form)
        QtCore.QMetaObject.connectSlotsByName(window_form)

    def retranslateUi(self, window_form):
        _translate = QtCore.QCoreApplication.translate
        window_form.setWindowTitle(_translate("window_form", "Марковские процессы"))
        self.state_count_label.setText(_translate("window_form", "Количество состояний:"))
        self.run_button.setText(_translate("window_form", "Запуск системы"))
        self.average_time_label.setText(_translate("window_form", "Среднее относительное время"))

    def calculate(self):
        try:
            matrix_size = self.input_table.rowCount()
            coefficients = matrix(numpy.zeros((matrix_size, matrix_size)))
            values = numpy.zeros(matrix_size)
            values[-1] = 1
            for i in range(matrix_size - 1):
                for j in range(matrix_size):
                    if i == j:
                        sum_intens = 0
                        for k in range(matrix_size):
							# if k != i: // if you don't want to have self-connections
                            sum_intens += float(self.input_table.item(i, k).text())
                        coefficients[i, j] = -sum_intens
                    else:
                        coefficients[i, j] = float(self.input_table.item(j, i).text())
            for i in range(matrix_size):
                coefficients[-1, i] = 1
            solution = solve(coefficients, values)
            for i in range(matrix_size):
                self.output_table.setItem(0, i, QtWidgets.QTableWidgetItem('%.2f' % solution[i]))
        except numpy.linalg.LinAlgError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Для данной матрицы состояний не удайтся найти решение.")
            msg.setInformativeText("Необходимо, чтобы был возможен переход\nиз каждого состояние "
                                   "в каждое за конечное число шагов")
            msg.setWindowTitle("Недостаточно данных")
            msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def output_table_zero(self):
        self.output_table.setItem(0, 0, QtWidgets.QTableWidgetItem('1'))
        for i in range(1, self.output_table.columnCount()):
            self.output_table.setItem(0, i, QtWidgets.QTableWidgetItem('0'))

    def input_table_zero(self):
        for i in range(self.input_table.rowCount()):
            for j in range(self.input_table.columnCount()):
                self.input_table.setItem(i, j, QtWidgets.QTableWidgetItem('0'))

    def tables_init(self):
        self.input_table.setRowCount(self.state_count_spinbox.value())
        self.input_table.setColumnCount(self.state_count_spinbox.value())
        self.output_table.setColumnCount(self.state_count_spinbox.value())
        self.input_table_zero()
        self.output_table_zero()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_form = QtWidgets.QWidget()
    ui = Ui_window_form()
    ui.setupUi(window_form)
    window_form.show()
    sys.exit(app.exec_())
