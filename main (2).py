import sys  # sys нужен для передачи argv в QApplication
import subprocess, io
import platform
import webbrowser, os  # работа с папками и файлами
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QCheckBox
from PyQt5.QtCore import QCoreApplication
import design  # Это наш конвертированный файл дизайна
import urllib.request


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QIcon('main.png'))
        self.pushButton.clicked.connect(self.browse_folder)
        # Менюбар

    def browse_folder(self):
        qw = str(self.lineEdit_2.text())
        self.lineEdit_2.settext(self.lineEdit.text())
        self.lineEdit.settext(qw)
        self.pushButton.setText("MainWindow", "<-")
        ExampleApp().show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExampleApp()
    ex.show()
    sys.exit(app.exec())
