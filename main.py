import time

import requests as req
import json

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

path_for_coinbase = 'CoinBase.json'
path_for_tradeogre = 'TradeOgre.json'

class DataThread(QThread):
    setText = pyqtSignal(str)

    def __init__(self, text, parent=None):
        super().__init__()
        self.text = text

    def run(self):
        while True:
            self.text = ''
            with open(path_for_tradeogre, 'r') as f:
                self.data = json.loads(f.read())
                for value in self.data:
                    resp = req.get(self.data[value]).json()
                    price = resp.get('price')
                    self.text += 'Стоимость валюты {} в биткоинах: {}'.format(value, price) + '\n'
            with open(path_for_coinbase, 'r') as f:
                self.data = json.loads(f.read())
                for value in self.data:
                    resp = req.get(self.data[value]).json()
                    price = float(resp.get('data').get('amount'))
                    if resp.get('data').get('currency') == 'RUB':
                        self.text += 'Стоимость валюты {}: {} рублей'.format(value, "{:,.0f}".format(price)) + '\n'
                    elif resp.get('data').get('currency') == 'USD':
                        self.text += 'Стоимость валюты {}: {} долларов'.format(value, "{:,.0f}".format(price)) + '\n'
                    else:
                        print('Нет такой валюты)')
            self.setText.emit(self.text)
            time.sleep(10)


class Ui_MainWindow(object):
    # TODO Сделать нормальный интерфейс
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(400, 450)
        MainWindow.setMinimumSize(QtCore.QSize(400, 450))
        MainWindow.setMaximumSize(QtCore.QSize(400, 450))
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.text = ''
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 370, 200, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.setText)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 400, 350))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.progress = QtWidgets.QProgressBar()

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Криптовалютный парсер"))
        self.pushButton.setText(_translate("MainWindow", "Вывод данных"))


    def setText(self):
        self.TextEd = DataThread(self.text)
        self.TextEd.setText.connect(self.TextToEditor)
        self.TextEd.start()

    def TextToEditor(self, text):
        self.textBrowser.setText(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
