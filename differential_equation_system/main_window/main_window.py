from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from math import exp, sin

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
        self.main_u10_label = QtWidgets.QLabel(self.main_koshi_task)
        self.main_u10_label.setObjectName("main_u10_label")
        self.gridLayout_12.addWidget(self.main_u10_label, 1, 0, 1, 1)
        self.main_u10_input = QtWidgets.QLineEdit(self.main_koshi_task)
        self.main_u10_input.setObjectName("main_u10_input")
        self.gridLayout_12.addWidget(self.main_u10_input, 1, 1, 1, 1)
        self.main_u20_label = QtWidgets.QLabel(self.main_koshi_task)
        self.main_u20_label.setObjectName("main_u20_label")
        self.gridLayout_12.addWidget(self.main_u20_label, 2, 0, 1, 1)
        self.main_u20_input = QtWidgets.QLineEdit(self.main_koshi_task)
        self.main_u20_input.setObjectName("main_u20_input")
        self.gridLayout_12.addWidget(self.main_u20_input, 2, 1, 1, 1)
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
        self.main_a_label = QtWidgets.QLabel(self.main_alghoritm_params)
        self.main_a_label.setObjectName("main_a_label")
        self.gridLayout_13.addWidget(self.main_a_label, 4, 0, 1, 1)
        self.main_a_input = QtWidgets.QLineEdit(self.main_alghoritm_params)
        self.main_a_input.setObjectName("main_a_input")
        self.gridLayout_13.addWidget(self.main_a_input, 4, 1, 1, 1)
        self.gridLayout_11.addWidget(self.main_alghoritm_params, 1, 1, 1, 1)
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

        self.info_tab = QtWidgets.QWidget()
        self.info_tab.setObjectName("info_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.info_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.info = QtWidgets.QTextEdit(self.info_tab)
        self.info.setReadOnly(True)
        self.info.setObjectName("info")
        self.gridLayout_8.addWidget(self.info, 0, 0, 1, 1)
        self.main_task.addTab(self.info_tab, "")
        self.task_swith.addTab(self.main_tab, "")
        self.gridLayout.addWidget(self.task_swith, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.task_swith.setCurrentIndex(0)
        self.main_task.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Численные методы. Лабораторная работа 1. Решение системы ДУ методом РК 4 порядка"))
        self.main_description.setHtml(_translate("MainWindow",""" <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; font-weight:600;">Описание основной задачи</span></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Рассматривается дифференциальное уравнение:</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">d</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">2</span><span style=" font-size:14pt; font-weight:600;">u/dx</span><span style=" font-size:14pt; font-weight:600; vertical-align:super;">2</span><span style=" font-size:14pt; font-weight:600;"> + a * sin(u) = 0</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u(0) = u</span><span style=" font-size:14pt; font-weight:600; vertical-align:sub;">0</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600;">u'(0) = u'</span><span style=" font-size:14pt; font-weight:600; vertical-align:sub;">0</span></p></body></html>"""))
        self.main_koshi_task.setTitle(_translate("MainWindow", "Задача Коши"))
        self.main_x0_label.setText(_translate("MainWindow", "<html><head/><body><p>x<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.main_x0_input.setText(_translate("MainWindow", "0"))
        self.main_u10_label.setText(_translate("MainWindow", "<html><head/><body><p>u<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.main_u10_input.setText(_translate("MainWindow", "1"))
        self.main_u20_label.setText(_translate("MainWindow", "<html><head/><body><p>u'<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.main_u20_input.setText(_translate("MainWindow", "1"))
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
        self.main_a_label.setText(_translate("MainWindow", "Параметр"))
        self.main_a_input.setText(_translate("MainWindow", "1"))
        self.main_graphics_box.setTitle(_translate("MainWindow", "График"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_task_tab), _translate("MainWindow", "Задача"))
        self.main_task.setTabText(self.main_task.indexOf(self.main_table_tab), _translate("MainWindow", "Таблица"))
        self.main_task.setTabText(self.main_task.indexOf(self.info_tab), _translate("MainWindow", "Справка"))
        self.task_swith.setTabText(self.task_swith.indexOf(self.main_tab), _translate("MainWindow", "Основная задача"))

    def get_stats(self, x_list : list, s_list : list, h_list : list, c1_list : list, c2_list : list):
        number_iter = len(s_list)
        max_x = 0
        max_s = s_list[0]
        max_h = h_list[0]
        min_h = h_list[0]
        c1_count = 0
        c2_count = 0
        for i in range(number_iter):
            if (max_s < s_list[i]):
                max_x = x_list[i]
                max_s = s_list[i]
            max_h = max(max_h, h_list[i])
            min_h = min(min_h, h_list[i])
            c1_count += c1_list[i]
            c2_count += c2_list[i]
        return max_s, max_x, max_h, min_h, c1_count, c2_count, number_iter

    def update_info(self, x_last, v1_last, v2_last, max_s : float, max_x : float, max_h : float, min_h : float, c1 : int, c2 : int, iter_count : int):
        self.info.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Полученное время (с): </span><span style=" font-size:14pt; font-weight:600;">""" + str(x_last) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Полученное положение (м): </span><span style=" font-size:14pt; font-weight:600;">""" + str(v2_last) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Полученное ускорение (м/с^2): </span><span style=" font-size:14pt; font-weight:600;">""" + str(v1_last) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Максимальная норма оценки локальной погрешности </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_s) +"""</span><span style=" font-size:14pt;"> достигнута при времени </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_x) +"""</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Максимальный шаг: </span><span style=" font-size:14pt; font-weight:600;">""" + str(max_h) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Минимальный шаг: </span><span style=" font-size:14pt; font-weight:600;">""" + str(min_h) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество раз, когда шаг увеличивался: </span><span style=" font-size:14pt; font-weight:600;">""" + str(c2) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество раз, когда шаг уменьшался: </span><span style=" font-size:14pt; font-weight:600;">""" + str(c1) + """</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">Количество итераций: </span><span style=" font-size:14pt; font-weight:600;">""" + str(iter_count - 1) + """</span></p></body></html>""")

    def plot(self, x_list : list, v1_list : list, v2_list : list):
        self.main_figure.clear()
        v1_v2 = self.main_figure.add_subplot(211)
        v1_v2.set_xlabel("V1")
        v1_v2.set_ylabel("V2")
        v1_v2.grid(True)
        v1_v2.plot(v1_list, v2_list)
        x_v1 = self.main_figure.add_subplot(223)
        x_v1.set_xlabel("X")
        x_v1.set_ylabel("V1")
        x_v1.grid(True)
        x_v1.plot(x_list, v1_list)
        x_v2 = self.main_figure.add_subplot(224)
        x_v2.set_xlabel("X")
        x_v2.set_ylabel("V2")
        x_v2.grid(True)
        x_v2.plot(x_list, v2_list)
        self.main_graphic.draw()
    
    def parse_main_start_values(self):
        x0 = float(self.main_x0_input.text())
        u10 = float(self.main_u10_input.text())
        u20 = float(self.main_u20_input.text())
        niter = int(self.main_niter_input.text())
        right_break = float(self.main_right_break_input.text())
        h0 = float(self.main_h0_input.text())
        epsilon = float(self.main_epsilon_input.text())
        a = float(self.main_a_input.text())
        return x0, u10, u20, niter, right_break, h0, epsilon, a

    def f1_main(self, x, u1, u2, a):
        return u2
    
    def f2_main(self, x, u1, u2, a):
        return -1 * a * sin(u1)

    def k1(self, x : float, u1 : float, u2 : float, h : float, a : float, f):
        return f(x, u1, u2, a)
    
    def k2(self, x : float, u1 : float, u2 : float, h : float, a : float, k11, k12, f):
        return f(x + h / 2, u1 + k11 * h/ 2, u2 + k12 * h / 2, a)

    def k3(self, x : float, u1 : float, u2 : float, h : float, a : float, k21, k22, f):
        return f(x + h / 2, u1 + k21 * h / 2, u2 + k22 * h / 2, a)

    def k4(self, x : float, u1 : float, u2 : float, h : float, a : float, k31, k32, f):
        return f(x + h, u1 + k31 * h, u2 + k32 * h, a)

    def calculate_iter_rk4(self, x_curr : float, v1_curr : float, v2_curr : float, h_curr : float, a :float, f1, f2):
        k11 = self.k1(x_curr, v1_curr, v2_curr, h_curr, a, f1)
        k12 = self.k1(x_curr, v1_curr, v2_curr, h_curr, a, f2)
        
        k21 = self.k2(x_curr, v1_curr, v2_curr, h_curr, a, k11, k12, f1)
        k22 = self.k2(x_curr, v1_curr, v2_curr, h_curr, a, k11, k12, f2)

        k31 = self.k3(x_curr, v1_curr, v2_curr, h_curr, a, k21, k22, f1)
        k32 = self.k3(x_curr, v1_curr, v2_curr, h_curr, a, k21, k22, f2)

        k41 = self.k4(x_curr, v1_curr, v2_curr, h_curr, a, k31, k32, f1)
        k42 = self.k4(x_curr, v1_curr, v2_curr, h_curr, a, k31, k32, f2)

        x_next = x_curr + h_curr
        v1_next = v1_curr + (k11 + k21 * 2 + k31 * 2 + k41) * h_curr / 6
        v2_next = v2_curr + (k12 + k22 * 2 + k32 * 2 + k42) * h_curr / 6
        return x_next, v1_next, v2_next
    
    def calculate_rk4_h_const(self, x0 : float, u10 : float, u20 : float, h0 : float, niter : int, right_break : float, a : float, f1, f2):
        x_list = [x0]
        v1_list = [u10]
        v2_list = [u20]
        v12_list = [u10]
        v22_list = [u20]
        dv1_list = [0]
        dv2_list = [0]
        s_list = [0]
        h_list = [h0]
        c1_list = [0]
        c2_list = [0]

        x_curr = x0
        v1_curr = u10
        v2_curr = u20
        
        for i in range(niter):
            if right_break <= x_curr: break
            try:
                x_next, v1_next, v2_next = self.calculate_iter_rk4(x_curr, v1_curr, v2_curr, h0, a, f1, f2)
                
                x05, v105, v205 = self.calculate_iter_rk4(x_curr, v1_curr, v2_curr, h0 / 2, a, f1, f2)
                _, v1205, v2205 = self.calculate_iter_rk4(x05, v105, v205, h0 / 2, a, f1, f2)

                x_curr = x_next
                v1_curr = v1_next
                v2_curr = v2_next

                x_list.append(x_curr)
                v1_list.append(v1_curr)
                v2_list.append(v2_curr)
                v12_list.append(v1205)
                v22_list.append(v2205)
                dv1_list.append(v1_curr - v1205)
                dv2_list.append(v2_curr - v2205)
                s_list.append(max(abs(v1_next - v1205), abs(v2_next - v2205)) / 15)
                h_list.append(h0)
                c1_list.append(0)
                c2_list.append(0)
            except Exception:
                break
        return x_list, v1_list, v2_list, v12_list, v22_list, dv1_list, dv2_list, s_list, h_list, c1_list, c2_list

    def calculate_rk4(self, x0 : float, u10 : float, u20 : float, h0 : float, epsilon : float, niter : int, right_break : float, a : float, f1, f2):
        x_list = [x0]
        v1_list = [u10]
        v2_list = [u20]
        v12_list = [u10]
        v22_list = [u20]
        dv1_list = [0]
        dv2_list = [0]
        s_list = [0]
        h_list = [h0]
        c1_list = [0]
        c2_list = [0]

        x_curr = x0
        v1_curr = u10
        v2_curr = u20
        h_curr = h0

        for i in range(niter):
            if right_break <= x_curr: break
            try:
                s_curr = 0
                c1_curr = 0
                c2_curr = 0
                while (True):
                    x_next, v1_next, v2_next = self.calculate_iter_rk4(x_curr, v1_curr, v2_curr, h_curr, a, f1, f2)
                    
                    x05, v105, v205 = self.calculate_iter_rk4(x_curr, v1_curr, v2_curr, h_curr / 2, a, f1, f2)
                    _, v1205, v2205 = self.calculate_iter_rk4(x05, v105, v205, h_curr / 2, a, f1, f2)

                    s_curr = (max(abs(v1_next - v1205), abs(v2_next - v2205))) / 15
                    if epsilon < s_curr:
                        c1_curr += 1
                        h_curr /= 2
                        continue
                    if epsilon / 15 <= s_curr <= epsilon:
                        h_next = h_curr
                        break
                    if s_curr < epsilon / 15:
                        c2_curr += 1
                        h_next = h_curr * 2
                        break
                
                x_curr = x_next
                v1_curr = v1_next
                v2_curr = v2_next
                h_list.append(h_curr)
                h_curr = h_next

                x_list.append(x_curr)
                v1_list.append(v1_curr)
                v2_list.append(v2_curr)
                v12_list.append(v1205)
                v22_list.append(v2205)
                dv1_list.append(v1_curr - v1205)
                dv2_list.append(v2_curr - v2205)
                s_list.append(s_curr)
                c1_list.append(c1_curr)
                c2_list.append(c2_curr)
            except Exception:
                break
        return x_list, v1_list, v2_list, v12_list, v22_list, dv1_list, dv2_list, s_list, h_list, c1_list, c2_list
    
    def main_calculate(self):
        x0, u10, u20, niter, right_break, h0, epsilon, a = self.parse_main_start_values()
        if 0 == epsilon:
            x_list, v1_list, v2_list, v12_list, v22_list, dv1_list, dv2_list, s_list, h_list, c1_list, c2_list = self.calculate_rk4_h_const(x0, u20, -1 * a * sin(u10), h0, niter, right_break, a, self.f1_main, self.f2_main)
            self.main_table.print_table(x_list, v1_list, v2_list, v12_list, v22_list, dv1_list, dv2_list, s_list, h_list, c1_list, c2_list)
            self.update_info(x_list[-1], v1_list[-1], v2_list[-1], *self.get_stats(x_list, s_list, h_list, c1_list, c2_list))
            self.plot(x_list, v1_list, v2_list)
        else:
            x_list, v1_list, v2_list, v12_list, v22_list, dv1_list, dv2_list, s_list, h_list, c1_list, c2_list = self.calculate_rk4(x0, u20, -1 * a * sin(u10), h0, epsilon, niter, right_break, a, self.f1_main, self.f2_main)
            self.main_table.print_table(x_list, v1_list, v2_list, v12_list, v22_list, dv1_list, dv2_list, s_list, h_list, c1_list, c2_list)
            self.update_info(x_list[-1], v1_list[-1], v2_list[-1], *self.get_stats(x_list, s_list, h_list, c1_list, c2_list),)
            self.plot(x_list, v1_list, v2_list)