from PyQt5 import QtCore, QtWidgets

class main_table(QtWidgets.QTableWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.row_count = 0
        self.col_count = 12
        self.setRowCount(self.row_count)
        self.setColumnCount(self.col_count)
        self.setHorizontalHeaderLabels(("Xi", "V1i", "V2i", "V1_2i", "V2_2i", "V1i - V1_2i", "V2i - V2_2i", "ОЛП", "Hi", "C1", "C2", "Mакс ОЛП"))

    def _create_cell(self, text):
        cell = QtWidgets.QTableWidgetItem(text)
        cell.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        return cell

    def _clear_table(self):
        for i in range(self.row_count):
            for j in range(self.col_count):
                self.setItem(i, j, self._create_cell(""))

    def print_table(self, x_list : list, v1_list : list, v2_list : list, v12_list : list,
                    v22_list : list, dv1_list : list, dv2_list : list, s_list : list, h_list : list,
                    c1_list : list, c2_list : list):
        self._clear_table()
        self.row_count = len(x_list)
        self.setRowCount(self.row_count)
        max = s_list[0]
        for i in range(self.row_count):
            self.setItem(i, 0, self._create_cell(str(x_list[i])))
            self.setItem(i, 1, self._create_cell(str(v1_list[i])))
            self.setItem(i, 2, self._create_cell(str(v2_list[i])))
            self.setItem(i, 3, self._create_cell(str(v12_list[i])))
            self.setItem(i, 4, self._create_cell(str(v22_list[i])))
            self.setItem(i, 5, self._create_cell(str(dv1_list[i])))
            self.setItem(i, 6, self._create_cell(str(dv2_list[i])))
            self.setItem(i, 7, self._create_cell(str(s_list[i])))
            self.setItem(i, 8, self._create_cell(str(h_list[i])))
            self.setItem(i, 9, self._create_cell(str(c1_list[i])))
            self.setItem(i, 10, self._create_cell(str(c2_list[i])))
            if (max < s_list[i]):
                max = s_list[i]
        self.setItem(0, 11, self._create_cell(str(max)))
