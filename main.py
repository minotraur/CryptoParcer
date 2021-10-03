import requests as req
import json

from PyQt5 import QtCore, QtWidgets

path_for_coinbase = 'CoinBase.json'
path_for_tradeogre = 'TradeOgre.json'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(400, 450)
        MainWindow.setMinimumSize(QtCore.QSize(400, 450))
        MainWindow.setMaximumSize(QtCore.QSize(400, 450))
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 370, 200, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 370, 200, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['TradeOgre', 'CoinBase'])
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.data_from_json()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Криптовалютный парсер"))
        self.pushButton.setText(_translate("MainWindow", "Вывод данных"))

    # TODO сделать очищение textBrowser и выбор биржи с помощью comboBox
    def data_from_json(self):
        # Сравниваем если текущий текст в comboBox == бирже, то должны выдаться данные с этой биржы.
        if self.comboBox.currentText() == 'TradeOgre':
            self.pushButton.clicked.connect(lambda: self.get_price_from_tradeogre())
        elif self.comboBox.currentText() == 'CoinBase':
            self.pushButton.clicked.connect(lambda: self.get_price_from_coinbase())
        else:
            print('Ошибка!')

    def get_price_from_coinbase(self):
        self.text = ''
        with open(path_for_coinbase, 'r') as f:
            self.data = json.loads(f.read())
            for value in self.data:
                resp = req.get(self.data[value]).json()
                price = float(resp.get('data').get('amount'))
                if resp.get('data').get('currency') == 'RUB':
                    self.text += 'Стоимость валюты {}: {} рублей'.format(value, "{:,.0f}".format(price)) + '\n'
                    self.textBrowser.setText(self.text)
                elif resp.get('data').get('currency') == 'USD':
                    self.text += 'Стоимость валюты {}: {} долларов'.format(value, "{:,.0f}".format(price)) + '\n'
                    self.textBrowser.setText(self.text)
                else:
                    print('Нет такой валюты)')

    def get_price_from_tradeogre(self):
        self.text = ''
        with open(path_for_tradeogre, 'r') as f:
            self.data = json.loads(f.read())
            for value in self.data:
                resp = req.get(self.data[value]).json()
                price = resp.get('price')
                self.text += 'Стоимость валюты {} в биткоинах: {}'.format(value, price) + '\n'
                self.textBrowser.setText(self.text)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
