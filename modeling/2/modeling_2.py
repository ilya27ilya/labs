#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modeling_2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import math
from bitarray import bitarray


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 465)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(480, 465))
        Form.setMaximumSize(QtCore.QSize(480, 465))
        Form.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.algorithm_input_table = QtWidgets.QTableWidget(Form)
        self.algorithm_input_table.setGeometry(QtCore.QRect(10, 40, 185, 330))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm_input_table.sizePolicy().hasHeightForWidth())
        self.algorithm_input_table.setSizePolicy(sizePolicy)
        self.algorithm_input_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.algorithm_input_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.algorithm_input_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.algorithm_input_table.setCornerButtonEnabled(False)
        self.algorithm_input_table.setRowCount(15)
        self.algorithm_input_table.setColumnCount(3)
        self.algorithm_input_table.setObjectName("algorithm_input_table")
        self.algorithm_input_table.horizontalHeader().setVisible(True)
        self.algorithm_input_table.horizontalHeader().setDefaultSectionSize(60)
        self.algorithm_input_table.horizontalHeader().setMinimumSectionSize(60)
        self.algorithm_input_table.verticalHeader().setVisible(False)
        self.algorithm_input_table.verticalHeader().setDefaultSectionSize(20)
        self.algorithm_input_table.verticalHeader().setMinimumSectionSize(20)
        self.algorithm_estimate_table = QtWidgets.QTableWidget(Form)
        self.algorithm_estimate_table.setGeometry(QtCore.QRect(10, 380, 185, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm_estimate_table.sizePolicy().hasHeightForWidth())
        self.algorithm_estimate_table.setSizePolicy(sizePolicy)
        self.algorithm_estimate_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.algorithm_estimate_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.algorithm_estimate_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.algorithm_estimate_table.setCornerButtonEnabled(False)
        self.algorithm_estimate_table.setRowCount(1)
        self.algorithm_estimate_table.setColumnCount(3)
        self.algorithm_estimate_table.setObjectName("algorithm_estimate_table")
        self.algorithm_estimate_table.horizontalHeader().setVisible(False)
        self.algorithm_estimate_table.horizontalHeader().setDefaultSectionSize(60)
        self.algorithm_estimate_table.horizontalHeader().setMinimumSectionSize(60)
        self.algorithm_estimate_table.verticalHeader().setVisible(False)
        self.algorithm_estimate_table.verticalHeader().setDefaultSectionSize(30)
        self.algorithm_estimate_table.verticalHeader().setMinimumSectionSize(30)
        self.manual_input_table = QtWidgets.QTableWidget(Form)
        self.manual_input_table.setGeometry(QtCore.QRect(410, 40, 65, 330))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_input_table.sizePolicy().hasHeightForWidth())
        self.manual_input_table.setSizePolicy(sizePolicy)
        self.manual_input_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.manual_input_table.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.manual_input_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.manual_input_table.setRowCount(15)
        self.manual_input_table.setColumnCount(1)
        self.manual_input_table.setObjectName("manual_input_table")
        self.manual_input_table.horizontalHeader().setVisible(True)
        self.manual_input_table.horizontalHeader().setDefaultSectionSize(60)
        self.manual_input_table.horizontalHeader().setMinimumSectionSize(60)
        self.manual_input_table.verticalHeader().setVisible(False)
        self.manual_input_table.verticalHeader().setDefaultSectionSize(20)
        self.manual_input_table.verticalHeader().setMinimumSectionSize(20)
        self.manual_estimate_table = QtWidgets.QTableWidget(Form)
        self.manual_estimate_table.setGeometry(QtCore.QRect(410, 380, 65, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_estimate_table.sizePolicy().hasHeightForWidth())
        self.manual_estimate_table.setSizePolicy(sizePolicy)
        self.manual_estimate_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.manual_estimate_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.manual_estimate_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.manual_estimate_table.setCornerButtonEnabled(False)
        self.manual_estimate_table.setRowCount(1)
        self.manual_estimate_table.setColumnCount(1)
        self.manual_estimate_table.setObjectName("manual_estimate_table")
        self.manual_estimate_table.horizontalHeader().setVisible(False)
        self.manual_estimate_table.horizontalHeader().setDefaultSectionSize(60)
        self.manual_estimate_table.horizontalHeader().setMinimumSectionSize(60)
        self.manual_estimate_table.verticalHeader().setVisible(False)
        self.manual_estimate_table.verticalHeader().setDefaultSectionSize(30)
        self.manual_estimate_table.verticalHeader().setMinimumSectionSize(30)
        self.algorithm_button = QtWidgets.QPushButton(Form)
        self.algorithm_button.setGeometry(QtCore.QRect(10, 420, 185, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm_button.sizePolicy().hasHeightForWidth())
        self.algorithm_button.setSizePolicy(sizePolicy)
        self.algorithm_button.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.algorithm_button.setObjectName("algorithm_button")
        self.manual_button = QtWidgets.QPushButton(Form)
        self.manual_button.setGeometry(QtCore.QRect(410, 420, 65, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_button.sizePolicy().hasHeightForWidth())
        self.manual_button.setSizePolicy(sizePolicy)
        self.manual_button.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.manual_button.setObjectName("manual_button")
        self.table_estimate_table = QtWidgets.QTableWidget(Form)
        self.table_estimate_table.setGeometry(QtCore.QRect(210, 380, 185, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_estimate_table.sizePolicy().hasHeightForWidth())
        self.table_estimate_table.setSizePolicy(sizePolicy)
        self.table_estimate_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_estimate_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_estimate_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_estimate_table.setCornerButtonEnabled(False)
        self.table_estimate_table.setRowCount(1)
        self.table_estimate_table.setColumnCount(3)
        self.table_estimate_table.setObjectName("table_estimate_table")
        self.table_estimate_table.horizontalHeader().setVisible(False)
        self.table_estimate_table.horizontalHeader().setDefaultSectionSize(60)
        self.table_estimate_table.horizontalHeader().setMinimumSectionSize(60)
        self.table_estimate_table.verticalHeader().setVisible(False)
        self.table_estimate_table.verticalHeader().setDefaultSectionSize(30)
        self.table_estimate_table.verticalHeader().setMinimumSectionSize(30)
        self.table_button = QtWidgets.QPushButton(Form)
        self.table_button.setGeometry(QtCore.QRect(210, 420, 185, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_button.sizePolicy().hasHeightForWidth())
        self.table_button.setSizePolicy(sizePolicy)
        self.table_button.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.table_button.setObjectName("table_button")
        self.table_input_table = QtWidgets.QTableWidget(Form)
        self.table_input_table.setGeometry(QtCore.QRect(210, 40, 185, 330))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_input_table.sizePolicy().hasHeightForWidth())
        self.table_input_table.setSizePolicy(sizePolicy)
        self.table_input_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_input_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_input_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_input_table.setCornerButtonEnabled(False)
        self.table_input_table.setRowCount(15)
        self.table_input_table.setColumnCount(3)
        self.table_input_table.setObjectName("table_input_table")
        self.table_input_table.horizontalHeader().setVisible(True)
        self.table_input_table.horizontalHeader().setDefaultSectionSize(60)
        self.table_input_table.horizontalHeader().setMinimumSectionSize(60)
        self.table_input_table.verticalHeader().setVisible(False)
        self.table_input_table.verticalHeader().setDefaultSectionSize(20)
        self.table_input_table.verticalHeader().setMinimumSectionSize(20)
        self.algorithm_label = QtWidgets.QLabel(Form)
        self.algorithm_label.setGeometry(QtCore.QRect(30, 10, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm_label.sizePolicy().hasHeightForWidth())
        self.algorithm_label.setSizePolicy(sizePolicy)
        self.algorithm_label.setObjectName("algorithm_label")
        self.table_label = QtWidgets.QLabel(Form)
        self.table_label.setGeometry(QtCore.QRect(220, 10, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_label.sizePolicy().hasHeightForWidth())
        self.table_label.setSizePolicy(sizePolicy)
        self.table_label.setAlignment(QtCore.Qt.AlignCenter)
        self.table_label.setObjectName("table_label")
        self.manual_input_label = QtWidgets.QLabel(Form)
        self.manual_input_label.setGeometry(QtCore.QRect(374, 10, 131, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_input_label.sizePolicy().hasHeightForWidth())
        self.manual_input_label.setSizePolicy(sizePolicy)
        self.manual_input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.manual_input_label.setObjectName("manual_input_label")
        self.retranslateUi(Form)
        self.algorithm_button.clicked.connect(self.generate_and_estimate_algorithm)
        self.table_button.clicked.connect(self.generate_and_estimate_table)
        self.manual_button.clicked.connect(self.estimate_manual)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def random_sequence_dec(self, count, size):
        if count <= 0 or size <= 0:
            raise ValueError
        random.seed()
        result = list()
        if size == 1:
            min_dec = 0
        else:
            min_dec = 10 ** (size - 1)
        max_dec = 10 ** size - 1
        for i in range(count):
            result.append(random.randint(min_dec, max_dec))
        return result

    def estimate_sequence_bin(self, sequence):
        s = 0
        n = len(sequence)
        for i in range(n):
            if sequence[i] == 1:
                s += 1
            else:
                s -= 1
        s_obs = abs(s) / math.sqrt(n)
        p = math.erfc(s_obs / math.sqrt(2))
        return p, p > 0.01

    def estimate_sequence_dec(self, sequence, min_dec, max_dec):
        sequence_bin = bitarray()
        for number in sequence:
            sequence_bin.extend('{0:b}'.format(number))
        return self.estimate_sequence_bin(sequence_bin)
        # m = (max_dec + min_dec) / 2
        # d = (max_dec - min_dec) ** 2 / 12
        # sigm = math.sqrt(d)
        # n = len(sequence)
        # my_m = 0
        # for number in sequence:
        #     my_m += number
        # my_m /= n
        # my_d = 0
        # for number in sequence:
        #     my_d += (number - my_m) ** 2
        # my_d /= n
        # my_sigm = math.sqrt(my_d)
        # if m == 0:
        #     rand_m = 0
        # else:
        #     rand_m = 1 - math.fabs(my_m - m) / m
        # if d == 0:
        #     rand_d = 0
        # else:
        #     rand_d = 1 - math.fabs(my_d - d) / d
        # count = 0
        # count_low = 0
        # count_high = 0
        # for number in sequence:
        #     if number >= m - sigm and number <= m + sigm:
        #         count += 1
        #     if number >= min_dec and number <= m:
        #         count_low += 1
        #     if number >= m and number <= max_dec:
        #         count_high += 1
        # rand_count = 1 - math.fabs((count / n) - 0.5774) / 0.5774
        # rand_low_high = 1 - abs(count_low - count_high) / n
        # return (rand_m + rand_d + rand_count + rand_low_high) / 4, rand_m > 0.5

    def generate_and_estimate_algorithm(self):
        one_digit_seq = self.random_sequence_dec(15, 1)
        two_digit_seq = self.random_sequence_dec(15, 2)
        three_digit_seq = self.random_sequence_dec(15, 3)
        for i in range(15):
            self.algorithm_input_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(one_digit_seq[i])))
            self.algorithm_input_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(two_digit_seq[i])))
            self.algorithm_input_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(three_digit_seq[i])))
        p, rand = self.estimate_sequence_dec(one_digit_seq, 0, 9)
        self.algorithm_estimate_table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(round(p * 100, 2))))
        p, rand = self.estimate_sequence_dec(two_digit_seq, 10, 99)
        self.algorithm_estimate_table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(round(p * 100, 2))))
        p, rand = self.estimate_sequence_dec(three_digit_seq, 100, 999)
        self.algorithm_estimate_table.setItem(0, 2, QtWidgets.QTableWidgetItem(str(round(p * 100, 2))))

    def generate_and_estimate_table(self):
        file = open('random.txt')
        text = file.read()
        file.close()
        text = text.replace(' ', '')
        text = text.replace('\n', '')
        text = text.strip(' \n')
        index = random.randint(0, len(text) - 1)
        one_digit_seq = list()
        for i in range(15):
            if index >= len(text):
                index = 0
            one_digit_seq.append(int(text[index]))
            index += 1
        index = random.randint(0, len(text) - 1)
        two_digit_seq = list()
        for i in range(15):
            if index >= len(text):
                index = 0
            two_digit_seq.append(int(text[index:index+2]))
            index += 2
        index = random.randint(0, len(text) - 1)
        three_digit_seq = list()
        for i in range(15):
            if index >= len(text):
                index = 0
            three_digit_seq.append(int(text[index:index + 3]))
            index += 3
        for i in range(15):
            self.table_input_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(one_digit_seq[i])))
            self.table_input_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(two_digit_seq[i])))
            self.table_input_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(three_digit_seq[i])))
        p, rand = self.estimate_sequence_dec(one_digit_seq, 0, 9)
        self.table_estimate_table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(round(p * 100, 2))))
        p, rand = self.estimate_sequence_dec(two_digit_seq, 10, 99)
        self.table_estimate_table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(round(p * 100, 2))))
        p, rand = self.estimate_sequence_dec(three_digit_seq, 100, 999)
        self.table_estimate_table.setItem(0, 2, QtWidgets.QTableWidgetItem(str(round(p * 100, 2))))

    def estimate_manual(self):
        sequence = list()
        for i in range(15):
            try:
                number = int(self.manual_input_table.item(i, 0).text())
                sequence.append(number)
            except Exception as e:
                pass
        if len(sequence) != 0:
            p, rand = self.estimate_sequence_dec(sequence, 0, 9)
        else:
            p = 0
        self.manual_estimate_table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(round(p * 100, 2))))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Случайные числа"))
        self.algorithm_button.setText(_translate("Form", "Сгенерировать и оценить"))
        self.manual_button.setText(_translate("Form", "Оценить"))
        self.table_button.setText(_translate("Form", "Сгенерировать и оценить"))
        self.algorithm_label.setText(_translate("Form", "Алгоритмический метод"))
        self.table_label.setText(_translate("Form", "Табличный метод"))
        self.manual_input_label.setText(_translate("Form", "Ручной ввод"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
