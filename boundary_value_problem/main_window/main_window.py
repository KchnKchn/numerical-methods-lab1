from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from math import exp, sin

import numpy as np

from tables import main_table
from tables import test_table
from solution import solution

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.task_swith = QtWidgets.QTabWidget(self.centralwidget)
        self.task_swith.setObjectName("task_swith")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.main_tab)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.main_task = QtWidgets.QTabWidget(self.main_tab)
        self.main_task.setObjectName("main_task")
        self.main_task_tab = QtWidgets.QWidget()
        self.main_task_tab.setObjectName("main_task_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.main_task_tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.main_description = QtWidgets.QTextEdit(self.main_task_tab)
        self.main_description.setReadOnly(True)
        self.main_description.setObjectName("main_description")
        self.gridLayout_10.addWidget(self.main_description, 2, 1, 1, 1)
        self.main_start_values = QtWidgets.QGroupBox(self.main_task_tab)
        self.main_start_values.setTitle("")
        self.main_start_values.setObjectName("main_start_values")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.main_start_values)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.main_n_label = QtWidgets.QLabel(self.main_start_values)
        self.main_n_label.setObjectName("main_n_label")
        self.gridLayout_11.addWidget(self.main_n_label, 0, 0)
        self.main_n_input = QtWidgets.QLineEdit(self.main_start_values)
        self.main_n_input.setObjectName("main_n_input")
        self.gridLayout_11.addWidget(self.main_n_input, 0, 1)
        self.main_start = QtWidgets.QPushButton(self.main_start_values)
        self.main_start.setObjectName("main_start")
        self.main_start.clicked.connect(self.main_calculate)
        self.gridLayout_11.addWidget(self.main_start, 1, 0, 1, 2)
        self.gridLayout_10.addWidget(self.main_start_values, 2, 0, 1, 1)
        self.main_graphics_box = QtWidgets.QGroupBox(self.main_task_tab)
        self.main_graphics_box.setObjectName("main_graphics_box")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.main_graphics_box)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.main_figure = Figure()
        self.main_graphic = FigureCanvas(self.main_figure)
        self.main_graphic.setObjectName("main_graphic")
        self.gridLayout_14.addWidget(self.main_graphic, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.main_graphics_box, 3, 0, 1, 2)
        self.main_task.addTab(self.main_task_tab, "")
        self.main_table_tab = QtWidgets.QWidget()
        self.main_table_tab.setObjectName("main_table_tab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.main_table_tab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.main_table = main_table.main_table(self.main_table_tab)
        self.main_table.setObjectName("main_table")
        self.gridLayout_15.addWidget(self.main_table, 0, 0, 1, 1)
        self.main_task.addTab(self.main_table_tab, "")
        self.gridLayout_17.addWidget(self.main_task, 0, 0, 1, 1)
        # self.task_swith.addTab(self.main_tab, "")
        self.test_tab = QtWidgets.QWidget()
        self.test_tab.setObjectName("test_tab")
        self.test_gridLayout_17 = QtWidgets.QGridLayout(self.test_tab)
        self.test_gridLayout_17.setObjectName("test_gridLayout_17")
        self.test_task = QtWidgets.QTabWidget(self.test_tab)
        self.test_task.setObjectName("test_task")
        self.test_task_tab = QtWidgets.QWidget()
        self.test_task_tab.setObjectName("test_task_tab")
        self.test_gridLayout_10 = QtWidgets.QGridLayout(self.test_task_tab)
        self.test_gridLayout_10.setObjectName("test_gridLayout_10")
        self.test_description = QtWidgets.QTextEdit(self.test_task_tab)
        self.test_description.setReadOnly(True)
        self.test_description.setObjectName("test_description")
        self.test_gridLayout_10.addWidget(self.test_description, 2, 1, 1, 1)
        self.test_start_values = QtWidgets.QGroupBox(self.test_task_tab)
        self.test_start_values.setTitle("")
        self.test_start_values.setObjectName("test_start_values")
        self.test_gridLayout_11 = QtWidgets.QGridLayout(self.test_start_values)
        self.test_gridLayout_11.setObjectName("test_gridLayout_11")
        self.test_n_label = QtWidgets.QLabel(self.test_start_values)
        self.test_n_label.setObjectName("test_n_label")
        self.test_gridLayout_11.addWidget(self.test_n_label, 0, 0)
        self.test_n_input = QtWidgets.QLineEdit(self.test_start_values)
        self.test_n_input.setObjectName("test_n_input")
        self.test_gridLayout_11.addWidget(self.test_n_input, 0, 1)
        self.test_start = QtWidgets.QPushButton(self.test_start_values)
        self.test_start.setObjectName("test_start")
        self.test_start.clicked.connect(self.test_calculate)
        self.test_gridLayout_11.addWidget(self.test_start, 1, 0, 1, 2)
        self.test_gridLayout_10.addWidget(self.test_start_values, 2, 0, 1, 1)
        self.test_graphics_box = QtWidgets.QGroupBox(self.test_task_tab)
        self.test_graphics_box.setObjectName("test_graphics_box")
        self.test_gridLayout_14 = QtWidgets.QGridLayout(self.test_graphics_box)
        self.test_gridLayout_14.setObjectName("test_gridLayout_14")
        self.test_figure = Figure()
        self.test_graphic = FigureCanvas(self.test_figure)
        self.test_graphic.setObjectName("test_graphic")
        self.test_gridLayout_14.addWidget(self.test_graphic, 1, 0, 1, 1)
        self.test_gridLayout_10.addWidget(self.test_graphics_box, 3, 0, 1, 2)
        self.test_task.addTab(self.test_task_tab, "")
        self.test_table_tab = QtWidgets.QWidget()
        self.test_table_tab.setObjectName("test_table_tab")
        self.test_gridLayout_15 = QtWidgets.QGridLayout(self.test_table_tab)
        self.test_gridLayout_15.setObjectName("test_gridLayout_15")
        self.test_table = test_table.test_table(self.test_table_tab)
        self.test_table.setObjectName("test_table")
        self.test_gridLayout_15.addWidget(self.test_table, 0, 0, 1, 1)
        self.test_task.addTab(self.test_table_tab, "")
        self.test_gridLayout_17.addWidget(self.test_task, 0, 0, 1, 1)
        self.task_swith.addTab(self.test_tab, "")
        self.main_info_tab = QtWidgets.QWidget()
        self.main_info_tab.setObjectName("main_info_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.main_info_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.main_info = QtWidgets.QTextEdit(self.main_info_tab)
        self.main_info.setReadOnly(True)
        self.main_info.setObjectName("main_info")
        self.gridLayout_5.addWidget(self.main_info, 0, 0, 1, 1)
        self.main_task.addTab(self.main_info_tab, "")
        self.test_info_tab = QtWidgets.QWidget()
        self.test_info_tab.setObjectName("test_info_tab")
        self.test_gridLayout_5 = QtWidgets.QGridLayout(self.test_info_tab)
        self.test_gridLayout_5.setObjectName("test_gridLayout_5")
        self.test_info = QtWidgets.QTextEdit(self.test_info_tab)
        self.test_info.setReadOnly(True)
        self.test_info.setObjectName("test_info")
        self.test_gridLayout_5.addWidget(self.test_info, 0, 0, 1, 1)
        self.test_task.addTab(self.test_info_tab, "")
        self.task_swith.addTab(self.main_tab, "")
        self.gridLayout.addWidget(self.task_swith, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.task_swith.setCurrentIndex(0)
        self.main_task.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Численные методы. Краевая задача"))
        self.main_description.setHtml(_translate("MainWindow","""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">Описание задачи</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Поставлена краевая задача:</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">(x + 1) * u''(x) - x * u = -x, x &lt;= ksi</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">x * u'' - x</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">2</span><span style=" font-size:14pt; font-weight:600;"> * u = -e</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">-x</span><span style=" font-size:14pt; font-weight:600;">, ksi &lt; x</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(0) = 0</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(1) = 1</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(ksi - 0) = u(ksi + 1)</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">(x + 1) * u'(x) = x * u'(x), x = ksi</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">ksi = 0.4</span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;"><br /></p></body></html>"""))
        
        self.test_description.setHtml(_translate("MainWindow","""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">Описание задачи</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Поставлена краевая задача:</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">1.4 * u''(x) - 0.4 * u = -0.4, x &lt;= ksi</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">0.4 * u'' - 0.4</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">2</span><span style=" font-size:14pt; font-weight:600;"> * u = -e</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">-0.4</span><span style=" font-size:14pt; font-weight:600;">, ksi &lt; x</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(0) = 0</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(1) = 1</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(ksi - 0) = u(ksi + 1)</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">(x + 1) * u'(x) = x * u'(x), x = ksi</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">ksi = 0.4</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Аналитическое решение:</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(x) = 0.06055722 * e</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">sqrt(2/7) * x</span><span style=" font-size:14pt; font-weight:600;"> - 1.06055722 * e</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">-sqrt(2/7) * x</span><span style=" font-size:14pt; font-weight:600;"> + 1, x &lt;=ksi</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(x) = -0.47202455 * e</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">sqrt(0.4) * x</span><span style=" font-size:14pt; font-weight:600;"> - 4.33108482 * e</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">-sqrt(0.4) * x</span><span style=" font-size:14pt; font-weight:600;"> + e</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">-0.4</span><span style=" font-size:14pt; font-weight:600;"> / 0.16, ksi &lt; x</span></p></body></html>"""))
        
        self.main_start.setText(_translate("MainWindow", "Численно вычислить"))
        self.main_n_label.setText(_translate("MainWindow", "Размер сетки"))
        self.main_n_input.setText(_translate("MainWindow", "10"))
        self.test_start.setText(_translate("MainWindow", "Численно вычислить"))
        self.test_n_label.setText(_translate("MainWindow", "Размер сетки"))
        self.test_n_input.setText(_translate("MainWindow", "10"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_task_tab), _translate("MainWindow", "Задача"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_table_tab), _translate("MainWindow", "Таблица"))
        self.test_task.setTabText(self.test_task.indexOf(self.test_task_tab), _translate("MainWindow", "Задача"))
        self.test_task.setTabText(self.test_task.indexOf(self.test_table_tab), _translate("MainWindow", "Таблица"))
        self.task_swith.setTabText(self.task_swith.indexOf(self.main_tab), _translate("MainWindow", "Основная задача"))
        self.task_swith.setTabText(self.task_swith.indexOf(self.test_tab), _translate("MainWindow", "Тестовая задача"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_info_tab), _translate("MainWindow", "Справка"))
        self.test_task.setTabText(self.test_task.indexOf(self.test_info_tab), _translate("MainWindow", "Справка"))

    def get_stats(self, n: int, x: np.array, v: np.array, v2: np.array):
        max_s = 0
        max_x = 0
        for i in range(n):
            if (max_s < abs(v[i] - v2[i])):
                max_s = abs(v[i] - v2[i])
                max_x = i / n
        return n, max_s, max_x

    def update_main_info(self, n: int, max_s: float, max_x: float):
        self.main_info.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Число разбиений: </span><span style=" font-size:14pt; font-weight:600;">""" + str(n) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Максимальная разность численных решений равна </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_s) +"""</span><span style=" font-size:14pt;"> наблюдается в точке </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_x) +"""</span></p>""")

    def update_test_info(self, n: int, max_s: float, max_x: float):
        self.test_info.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Число разбиений: </span><span style=" font-size:14pt; font-weight:600;">""" + str(n) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Максимальная разность аналитического и численного решений равна </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_s) +"""</span><span style=" font-size:14pt;"> наблюдается в точке </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_x) +"""</span></p>""")

    def main_plot(self, x: np.array, v: np.array, v2: np.array):
        self.main_figure.clear()
        ax = self.main_figure.add_subplot(211)
        ax2 = self.main_figure.add_subplot(212)
        ax.grid(True)
        ax.plot(x, v, label="Численное решение с одиночным шагом")
        ax.plot(x, v2, label="Численное решение с половинным шагом")
        ax.legend()
        ax2.grid(True)
        ax2.plot(x, v - v2, label="Разность численных решений")
        ax2.legend()
        self.main_graphic.draw()
    
    def test_plot(self, x: np.array, v: np.array, u: np.array):
        self.test_figure.clear()
        ax = self.test_figure.add_subplot(211)
        ax2 = self.test_figure.add_subplot(212)
        ax.grid(True)
        ax.plot(x, v, label="Численное решение")
        ax.plot(x, u, label="Точное решение")
        ax.legend()
        ax2.grid(True)
        ax2.plot(x, u - v, label="Глобальна погрешность в узлах сетки")
        ax2.legend()
        self.test_graphic.draw()

    def parse_main_n(self):
        return int(self.main_n_input.text())
    
    def parse_test_n(self):
        return int(self.test_n_input.text())

    def main_calculate(self):
        n = self.parse_main_n()
        x, v, v2 = solution.main_task(n)
        self.update_main_info(*self.get_stats(n, x, v, v2))
        self.main_table.print_table(x, v, v2, v - v2)
        self.main_plot(x, v, v2)
    
    def test_calculate(self):
        n = self.parse_test_n()
        x, v, u = solution.test_task(n)
        self.update_test_info(*self.get_stats(n, x, u, v))
        self.test_table.print_table(x, u, v, u - v)
        self.test_plot(x, v, u)