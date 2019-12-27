from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from math import exp, sin

from tables import test_table
from tables import main_table

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
        self.test_tab = QtWidgets.QWidget()
        self.test_tab.setObjectName("test_tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.test_tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.test_task = QtWidgets.QTabWidget(self.test_tab)
        self.test_task.setObjectName("test_task")
        self.test_task_tab = QtWidgets.QWidget()
        self.test_task_tab.setObjectName("test_task_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.test_task_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.test_description = QtWidgets.QTextEdit(self.test_task_tab)
        self.test_description.setReadOnly(True)
        self.test_description.setObjectName("test_description")
        self.gridLayout_2.addWidget(self.test_description, 2, 1, 1, 1)
        self.test_start_values = QtWidgets.QGroupBox(self.test_task_tab)
        self.test_start_values.setTitle("")
        self.test_start_values.setObjectName("test_start_values")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.test_start_values)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.test_koshi_task = QtWidgets.QGroupBox(self.test_start_values)
        self.test_koshi_task.setObjectName("test_koshi_task")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.test_koshi_task)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.test_x0_label = QtWidgets.QLabel(self.test_koshi_task)
        self.test_x0_label.setObjectName("test_x0_label")
        self.gridLayout_7.addWidget(self.test_x0_label, 0, 0, 1, 1)
        self.test_x0_input = QtWidgets.QLineEdit(self.test_koshi_task)
        self.test_x0_input.setObjectName("test_x0_input")
        self.gridLayout_7.addWidget(self.test_x0_input, 0, 1, 1, 1)
        self.test_u0_label = QtWidgets.QLabel(self.test_koshi_task)
        self.test_u0_label.setObjectName("test_u0_label")
        self.gridLayout_7.addWidget(self.test_u0_label, 1, 0, 1, 1)
        self.test_u0_input = QtWidgets.QLineEdit(self.test_koshi_task)
        self.test_u0_input.setObjectName("test_u0_input")
        self.gridLayout_7.addWidget(self.test_u0_input, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.test_koshi_task, 1, 0, 1, 1)
        self.test_start = QtWidgets.QPushButton(self.test_start_values)
        self.test_start.setObjectName("test_start")
        self.test_start.clicked.connect(self.test_calculate)
        self.gridLayout_4.addWidget(self.test_start, 2, 0, 1, 1)
        self.test_alghoritm_params = QtWidgets.QGroupBox(self.test_start_values)
        self.test_alghoritm_params.setObjectName("test_alghoritm_params")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.test_alghoritm_params)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.test_niter_label = QtWidgets.QLabel(self.test_alghoritm_params)
        self.test_niter_label.setObjectName("test_niter_label")
        self.gridLayout_8.addWidget(self.test_niter_label, 0, 0, 1, 1)
        self.test_right_break_label = QtWidgets.QLabel(self.test_alghoritm_params)
        self.test_right_break_label.setObjectName("test_right_break_label")
        self.gridLayout_8.addWidget(self.test_right_break_label, 1, 0, 1, 1)
        self.test_epsilon_label = QtWidgets.QLabel(self.test_alghoritm_params)
        self.test_epsilon_label.setObjectName("test_epsilon_label")
        self.gridLayout_8.addWidget(self.test_epsilon_label, 3, 0, 1, 1)
        self.test_h0_label = QtWidgets.QLabel(self.test_alghoritm_params)
        self.test_h0_label.setObjectName("test_h0_label")
        self.gridLayout_8.addWidget(self.test_h0_label, 2, 0, 1, 1)
        self.test_niter_input = QtWidgets.QLineEdit(self.test_alghoritm_params)
        self.test_niter_input.setObjectName("test_niter_input")
        self.gridLayout_8.addWidget(self.test_niter_input, 0, 1, 1, 1)
        self.test_right_break_input = QtWidgets.QLineEdit(self.test_alghoritm_params)
        self.test_right_break_input.setObjectName("test_right_break_input")
        self.gridLayout_8.addWidget(self.test_right_break_input, 1, 1, 1, 1)
        self.test_h0_input = QtWidgets.QLineEdit(self.test_alghoritm_params)
        self.test_h0_input.setObjectName("test_h0_input")
        self.gridLayout_8.addWidget(self.test_h0_input, 2, 1, 1, 1)
        self.test_epsilon_input = QtWidgets.QLineEdit(self.test_alghoritm_params)
        self.test_epsilon_input.setObjectName("test_epsilon_input")
        self.gridLayout_8.addWidget(self.test_epsilon_input, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.test_alghoritm_params, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.test_start_values, 2, 0, 1, 1)
        self.test_graphics_box = QtWidgets.QGroupBox(self.test_task_tab)
        self.test_graphics_box.setObjectName("test_graphics_box")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.test_graphics_box)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.test_figure = Figure()
        self.test_graphic = FigureCanvas(self.test_figure)
        self.test_ax = self.test_figure.add_subplot(111)
        #self.test_graphic = QtWidgets.QGraphicsView(self.test_graphics_box)
        self.test_graphic.setObjectName("test_graphic")
        self.gridLayout_6.addWidget(self.test_graphic, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.test_graphics_box, 3, 0, 1, 2)
        self.test_task.addTab(self.test_task_tab, "")
        self.test_table_tab = QtWidgets.QWidget()
        self.test_table_tab.setObjectName("test_table_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.test_table_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.test_table = test_table.test_table(self.test_table_tab)
        self.test_table.setObjectName("test_table")
        self.gridLayout_3.addWidget(self.test_table, 0, 0, 1, 1)
        self.test_task.addTab(self.test_table_tab, "")
        self.gridLayout_9.addWidget(self.test_task, 0, 0, 1, 1)
        self.task_swith.addTab(self.test_tab, "")
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
        self.main_koshi_task = QtWidgets.QGroupBox(self.main_start_values)
        self.main_koshi_task.setObjectName("main_koshi_task")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.main_koshi_task)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.main_x0_label = QtWidgets.QLabel(self.main_koshi_task)
        self.main_x0_label.setObjectName("main_x0_label")
        self.gridLayout_12.addWidget(self.main_x0_label, 0, 0, 1, 1)
        self.main_x0_input = QtWidgets.QLineEdit(self.main_koshi_task)
        self.main_x0_input.setObjectName("main_x0_input")
        self.gridLayout_12.addWidget(self.main_x0_input, 0, 1, 1, 1)
        self.main_u0_label = QtWidgets.QLabel(self.main_koshi_task)
        self.main_u0_label.setObjectName("main_u0_label")
        self.gridLayout_12.addWidget(self.main_u0_label, 1, 0, 1, 1)
        self.main_u0_input = QtWidgets.QLineEdit(self.main_koshi_task)
        self.main_u0_input.setObjectName("main_u0_input")
        self.gridLayout_12.addWidget(self.main_u0_input, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.main_koshi_task, 1, 0, 1, 1)
        self.main_start = QtWidgets.QPushButton(self.main_start_values)
        self.main_start.setObjectName("main_start")
        self.main_start.clicked.connect(self.main_calculate)
        self.gridLayout_11.addWidget(self.main_start, 2, 0, 1, 1)
        self.main_alghoritm_params = QtWidgets.QGroupBox(self.main_start_values)
        self.main_alghoritm_params.setObjectName("main_alghoritm_params")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.main_alghoritm_params)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.main_niter_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_niter_label.setObjectName("main_niter_label")
        self.gridLayout_13.addWidget(self.main_niter_label, 0, 0, 1, 1)
        self.main_right_break_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_right_break_label.setObjectName("main_right_break_label")
        self.gridLayout_13.addWidget(self.main_right_break_label, 1, 0, 1, 1)
        self.main_epsilon_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_epsilon_label.setObjectName("main_epsilon_label")
        self.gridLayout_13.addWidget(self.main_epsilon_label, 3, 0, 1, 1)
        self.main_h0_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_h0_label.setObjectName("main_h0_label")
        self.gridLayout_13.addWidget(self.main_h0_label, 2, 0, 1, 1)
        self.main_niter_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_niter_input.setObjectName("main_niter_input")
        self.gridLayout_13.addWidget(self.main_niter_input, 0, 1, 1, 1)
        self.main_right_break_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_right_break_input.setObjectName("main_right_break_input")
        self.gridLayout_13.addWidget(self.main_right_break_input, 1, 1, 1, 1)
        self.main_h0_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_h0_input.setObjectName("main_h0_input")
        self.gridLayout_13.addWidget(self.main_h0_input, 2, 1, 1, 1)
        self.main_epsilon_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_epsilon_input.setObjectName("main_epsilon_input")
        self.gridLayout_13.addWidget(self.main_epsilon_input, 3, 1, 1, 1)
        self.gridLayout_11.addWidget(self.main_alghoritm_params, 1, 1, 1, 1)
        self.gridLayout_10.addWidget(self.main_start_values, 2, 0, 1, 1)
        self.main_graphics_box = QtWidgets.QGroupBox(self.main_task_tab)
        self.main_graphics_box.setObjectName("main_graphics_box")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.main_graphics_box)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.main_figure = Figure()
        self.main_graphic = FigureCanvas(self.main_figure)
        self.main_ax = self.main_figure.add_subplot(111)
        #self.main_graphic = QtWidgets.QGraphicsView(self.main_graphics_box)
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
        self.task_swith.addTab(self.main_tab, "")
        self.gridLayout.addWidget(self.task_swith, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.task_swith.setCurrentIndex(0)
        self.test_task.setCurrentIndex(0)
        self.main_task.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Численные методы. Лабораторная работа 1. Решение ДУ методом РК 4 порядка"))
        self.test_description.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Описание тестовой задачи</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Рассматривается дифференциальное уравнение:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">du/dx = -1/2u<br />u(x</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:14pt; font-weight:600;\">) = u</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Точное решение задачи:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">u = u</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:14pt; font-weight:600;\">e</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">-x/2</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.test_koshi_task.setTitle(_translate("MainWindow", "Задача Коши"))
        self.test_x0_label.setText(_translate("MainWindow", "<html><head/><body><p>x<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.test_x0_input.setText(_translate("MainWindow", "0"))
        self.test_u0_label.setText(_translate("MainWindow", "<html><head/><body><p>u<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.test_u0_input.setText(_translate("MainWindow", "0"))
        self.test_start.setText(_translate("MainWindow", "Численно вычислить"))
        self.test_alghoritm_params.setTitle(_translate("MainWindow", "Параметры алгоритма"))
        self.test_niter_label.setText(_translate("MainWindow", "Количество итераций"))
        self.test_right_break_label.setText(_translate("MainWindow", "Правая граница"))
        self.test_epsilon_label.setText(_translate("MainWindow", "Контроль локальной погрешности"))
        self.test_h0_label.setText(_translate("MainWindow", "Шаг интегрирования"))
        self.test_niter_input.setText(_translate("MainWindow", "1000"))
        self.test_right_break_input.setText(_translate("MainWindow", "100"))
        self.test_h0_input.setText(_translate("MainWindow", "0.001"))
        self.test_epsilon_input.setText(_translate("MainWindow", "0"))
        self.test_graphics_box.setTitle(_translate("MainWindow", "График"))
        self.test_task.setTabText(self.test_task.indexOf(self.test_task_tab), _translate("MainWindow", "Задача"))
        self.test_task.setTabText(self.test_task.indexOf(self.test_table_tab), _translate("MainWindow", "Таблица"))
        self.task_swith.setTabText(self.task_swith.indexOf(self.test_tab), _translate("MainWindow", "Тестовая задача"))
        self.main_description.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Описание основной задачи</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Рассматривается дифференциальное уравнение:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">du/dx = (1+x</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">4</span><span style=\" font-size:14pt; font-weight:600;\">)</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">-1</span><span style=\" font-size:14pt; font-weight:600;\">u</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-size:14pt; font-weight:600;\"> + u - u</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">3</span><span style=\" font-size:14pt; font-weight:600;\">sin(10x)<br />u(x</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:14pt; font-weight:600;\">) = u</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">0</span></p></body></html>"))
        self.main_koshi_task.setTitle(_translate("MainWindow", "Задача Коши"))
        self.main_x0_label.setText(_translate("MainWindow", "<html><head/><body><p>x<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.main_x0_input.setText(_translate("MainWindow", "0"))
        self.main_u0_label.setText(_translate("MainWindow", "<html><head/><body><p>u<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.main_u0_input.setText(_translate("MainWindow", "0"))
        self.main_start.setText(_translate("MainWindow", "Численно вычислить"))
        self.main_alghoritm_params.setTitle(_translate("MainWindow", "Параметры алгоритма"))
        self.main_niter_label.setText(_translate("MainWindow", "Количество итераций"))
        self.main_right_break_label.setText(_translate("MainWindow", "Правая граница"))
        self.main_epsilon_label.setText(_translate("MainWindow", "Контроль локальной погрешности"))
        self.main_h0_label.setText(_translate("MainWindow", "Шаг интегрирования"))
        self.main_niter_input.setText(_translate("MainWindow", "1000"))
        self.main_right_break_input.setText(_translate("MainWindow", "100"))
        self.main_h0_input.setText(_translate("MainWindow", "0.001"))
        self.main_epsilon_input.setText(_translate("MainWindow", "0"))
        self.main_graphics_box.setTitle(_translate("MainWindow", "График"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_task_tab), _translate("MainWindow", "Задача"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_table_tab), _translate("MainWindow", "Таблица"))
        self.task_swith.setTabText(self.task_swith.indexOf(self.main_tab), _translate("MainWindow", "Основная задача"))
    
    def plot(self, graphic, ax, x_list : list, v_list : list, u_list : list):
        ax.clear()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        ax.plot(x_list, v_list, label = "Численное решение")
        if u_list:
            ax.plot(x_list, u_list, label = "Точное решение")
        ax.legend()
        graphic.draw()
    
    def parse_test_start_values(self):
        x0 = float(self.test_x0_input.text())
        u0 = float(self.test_u0_input.text())
        niter = int(self.test_niter_input.text())
        right_break = float(self.test_right_break_input.text())
        h0 = float(self.test_h0_input.text())
        epsilon = float(self.test_epsilon_input.text())
        return x0, u0, niter, right_break, h0, epsilon
    
    def parse_main_start_values(self):
        x0 = float(self.main_x0_input.text())
        u0 = float(self.main_u0_input.text())
        niter = int(self.main_niter_input.text())
        right_break = float(self.main_right_break_input.text())
        h0 = float(self.main_h0_input.text())
        epsilon = float(self.main_epsilon_input.text())
        return x0, u0, niter, right_break, h0, epsilon
    
    def u_test(self, x : float, u0 : float):
        return u0 / exp(x/2)
    
    def f_test(self, x : float, u : float):
        return -u / 2

    def f_main(self, x : float, u : float):
        s1 = u ** 2
        s2 = 1 + (x ** 4)
        s3 = u
        s4 = u ** 3
        s5 = sin(10 * x)
        result = s1 / s2 + s3 - s4 * s5
        return result
        #return (u ** 2) / (1 + (x ** 4)) + u - (u ** 3) * sin(10 * x)
    
    def calculate_u_test(self, x_list : list, u0 : list):
        u_list = []
        for i in range(len(x_list)):
            u_list.append(self.u_test(x_list[i], u0))
        return u_list
    
    def calculate_sub_u_v(self, u_list, v_list):
        sub_list = []
        for i in range(len(u_list)):
            sub_list.append(abs(u_list[i] - v_list[i]))
        return sub_list

    def k1(self, x : float, v : float, h : float, f):
        return f(x, v)
    
    def k2(self, x : float, v : float, h : float, k1 : float, f):
        return f(x + h / 2, v + k1 * h / 2)

    def k3(self, x : float, v : float, h : float, k2 : float, f):
        return f(x + h / 2, v + k2 * h / 2)

    def k4(self, x : float, v : float, h : float, k3 : float, f):
        return f(x + h, v + k3 * h)

    def calculate_iter_rk4(self, x_curr : float, v_curr : float, h_curr : float, f):
        k1 = self.k1(x_curr, v_curr, h_curr, f)
        k2 = self.k2(x_curr, v_curr, h_curr, k1, f)
        k3 = self.k3(x_curr, v_curr, h_curr, k2, f)
        k4 = self.k4(x_curr, v_curr, h_curr, k3, f)

        x_next = x_curr + h_curr
        v_next = v_curr + (k1 + k2 * 2 + k3 * 2 + k4) * h_curr / 6
        return x_next, v_next
    
    def calculate_rk4_h_const(self, x0 : float, u0 : float, h0 : float, niter : int, right_break : float, f):
        x_list = [x0]
        v_list = [u0]
        v2_list = [u0]
        dv_list = [0]
        s_list = [0]
        h_list = [h0]
        c1_list = [0]
        c2_list = [0]

        x_curr = x0
        v_curr = u0
        
        for i in range(niter):
            if right_break <= x_curr: break
            try:
                x_next, v_next = self.calculate_iter_rk4(x_curr, v_curr, h0, f)
                
                x05, v05 = self.calculate_iter_rk4(x_curr, v_curr, h0 / 2, f)
                _, v2_next = self.calculate_iter_rk4(x05, v05, h0 / 2, f)

                x_curr = x_next
                v_curr = v_next

                x_list.append(x_curr)
                v_list.append(v_curr)
                v2_list.append(v2_next)
                dv_list.append(v_curr - v2_next)
                s_list.append(abs((v_curr - v2_next) / 15))
                h_list.append(h0)
                c1_list.append(0)
                c2_list.append(0)
            except Exception:
                break
        return x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list

    def calculate_rk4(self, x0 : float, u0 : float, h0 : float, epsilon, niter : int, right_break : float, f):
        x_list = [x0]
        v_list = [u0]
        v2_list = [u0]
        dv_list = [0]
        s_list = [0]
        h_list = [h0]
        c1_list = [0]
        c2_list = [0]

        x_curr = x0
        v_curr = u0
        h_curr = h0

        for i in range(niter):
            if right_break <= x_curr: break
            try:
                s_curr = 0
                c1_curr = 0
                c2_curr = 0
                while (True):
                    x_next, v_next = self.calculate_iter_rk4(x_curr, v_curr, h_curr, f)
                    
                    x05, v05 = self.calculate_iter_rk4(x_curr, v_curr, h_curr / 2, f)
                    _, v2_next = self.calculate_iter_rk4(x05, v05, h_curr / 2, f)
                    s_curr = (v_next - v2_next) / 15
                    if epsilon < abs(s_curr):
                        c1_curr += 1
                        h_curr /= 2
                        continue
                    if epsilon / 15 <= abs(s_curr) <= epsilon:
                        h_next = h_curr
                        break
                    if abs(s_curr) < epsilon / 15:
                        h_next = h_curr * 2
                        c2_curr += 1
                        break

                x_curr = x_next
                v_curr = v_next
                h_list.append(h_curr)
                h_curr = h_next

                x_list.append(x_curr)
                v_list.append(v_curr)
                v2_list.append(v2_next)
                dv_list.append(v_curr - v2_next)
                s_list.append(abs((v_curr - v2_next) / 15))
                c1_list.append(c1_curr)
                c2_list.append(c2_curr)
            except Exception:
                break
        return x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list

    def test_calculate(self):
        x0, u0, niter, right_break, h0, epsilon = self.parse_test_start_values()
        const = u0 * exp(x0 / 2)
        if 0 == epsilon:
            x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list = self.calculate_rk4_h_const(x0, u0, h0, niter, right_break, self.f_test)
            u_list = self.calculate_u_test(x_list, const)
            epsilon_list = self.calculate_sub_u_v(u_list, v_list)
            self.test_table.print_table(x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list, u_list, epsilon_list)
            self.plot(self.test_graphic, self.test_ax, x_list, v_list, u_list)
        else:
            x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list = self.calculate_rk4(x0, u0, h0, epsilon, niter, right_break, self.f_test)
            u_list = self.calculate_u_test(x_list, const)
            epsilon_list = self.calculate_sub_u_v(u_list, v_list)
            self.test_table.print_table(x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list, u_list, epsilon_list)
            self.plot(self.test_graphic, self.test_ax, x_list, v_list, u_list)
    
    def main_calculate(self):
        x0, u0, niter, right_break, h0, epsilon = self.parse_main_start_values()
        if 0 == epsilon:
            x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list = self.calculate_rk4_h_const(x0, u0, h0, niter, right_break, self.f_main)
            self.main_table.print_table(x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list)
            self.plot(self.main_graphic, self.main_ax, x_list, v_list, None)
        else:
            x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list = self.calculate_rk4(x0, u0, h0, epsilon, niter, right_break, self.f_main)
            self.main_table.print_table(x_list, v_list, v2_list, dv_list, s_list, h_list, c1_list, c2_list)
            self.plot(self.main_graphic, self.main_ax, x_list, v_list, None)