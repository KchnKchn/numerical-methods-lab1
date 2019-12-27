from main_window import main_window as main

if __name__ == "__main__":
    import sys
    app = main.QtWidgets.QApplication(sys.argv)
    MainWindow = main.QtWidgets.QMainWindow()
    ui = main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())