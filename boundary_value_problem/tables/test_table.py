from PyQt5 import QtCore, QtWidgets
import numpy as np

class test_table(QtWidgets.QTableWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.row_count = 0
        self.col_count = 4
        self.setRowCount(self.row_count)
        self.setColumnCount(self.col_count)
        self.setHorizontalHeaderLabels(("Xi", "U(Xi)", "V(Xi)", "U(Xi) - V(Xi)"))
        self.resizeColumnsToContents()

    def _create_cell(self, text):
        cell = QtWidgets.QTableWidgetItem(text)
        cell.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        return cell

    def _clear_table(self):
        for i in range(self.row_count):
            for j in range(self.col_count):
                self.setItem(i, j, self._create_cell(""))

    def print_table(self, x: np.array, u: np.array, v: np.array, s: np.array):
        self._clear_table()
        self.row_count = x.shape[0]
        self.setRowCount(self.row_count)
        for i in range(self.row_count):
            self.setItem(i, 0, self._create_cell(str(x[i])))
            self.setItem(i, 1, self._create_cell(str(u[i])))
            self.setItem(i, 2, self._create_cell(str(v[i])))
            self.setItem(i, 3, self._create_cell(str(s[i])))
        self.resizeColumnsToContents()
