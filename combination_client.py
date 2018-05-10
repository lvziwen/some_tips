# -*- coding: utf-8 -*-
import sys
from itertools import combinations
from PyQt4 import QtGui, QtCore
class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle(u'组合数计算')
        seperate = QtGui.QLabel(u'分解数:')
        combination = QtGui.QLabel(u"组合数:")
        result = QtGui.QLabel(u"结果:")


        self.seperate = QtGui.QLineEdit()
        self.combination = QtGui.QLineEdit()
        self.result = QtGui.QTextEdit()
        grid = QtGui.QGridLayout()

        grid.addWidget(seperate, 1, 0)
        grid.addWidget(self.seperate, 1, 1)

        grid.addWidget(combination, 2, 0)
        grid.addWidget(self.combination, 2, 1)

        grid.addWidget(result, 3, 0)
        grid.addWidget(self.result, 3, 1)

        calc = QtGui.QPushButton(u'计算')
        grid.addWidget(calc, 4, 0)

        self.setLayout(grid)
        self.resize(800, 500)

        self.connect(calc, QtCore.SIGNAL('clicked()'), self.calc)

    def calc(self):
        seperate = self.seperate.text()
        combination = self.combination.text()

        seperate_list = [int(x) for x in seperate.split(",")]
        combination_list = [int(y) for y in combination.split(",")]

        len_l = len(seperate_list)
        len_r = len(combination_list)

        
        i = 2
        while i < len_l:
            comb_list = list(combinations(seperate_list, i))
            for item in comb_list:
                for r in combination_list:
                    if sum(item) == r:
                        self.result.append(str(item) + "=" + str(r))
            i += 1


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
        
