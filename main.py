import time

import requests as req
import json

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QThread, pyqtSignal

path_for_coinbase = 'Json\CoinBase.json'
#{'data': {'base': 'BTC', 'currency': 'RUB', 'amount': '4145594.69'}}
path_for_tradeogre = 'Json\TradeOgre.json'
#{'success': True, 'initialprice': '0.06252515', 'price': '0.06147607', 'high': '0.06422734', 'low': '0.05502624', 'volume': '3.39374699', 'bid': '0.06070103', 'ask': '0.06178323'}

class DataThread(QThread):
    setText = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__()

    def run(self):
        while True:
            text = ''
            with open(path_for_coinbase, 'r') as f:
                self.data = json.loads(f.read())
                for value in self.data:
                    text = value
                    response = req.get(self.data[value])
                    try:
                        response.raise_for_status()
                    except req.exceptions.HTTPError:
                        self.setText.emit(text, 'NDA ({}).'.format(response.status_code))
                        continue
                    resp = response.json()
                    price = '{}'.format("{:,.0f}".format(float(resp.get('data').get('amount'))))
                    self.setText.emit(text, price)
            with open(path_for_tradeogre, 'r') as f:
                self.data = json.loads(f.read())
                for value in self.data:
                    text = value
                    response = req.get(self.data[value])
                    try:
                        response.raise_for_status()
                    except req.exceptions.HTTPError:
                        self.setText.emit(text,'NDA ({}).'.format(response.status_code)+';'+'NDA ({})'.format(response.status_code))
                        continue
                    resp = response.json()
                    price = resp.get('price')+';'+resp.get('high')
                    self.setText.emit(text, price)

            #self.setText.emit(text,Abob)
            time.sleep(10)


class Ui_MainWindow(object):
    # TODO Сделать нормальный интерфейс
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(260, 560)
        MainWindow.setMinimumSize(QtCore.QSize(260, 560))
        MainWindow.setMaximumSize(QtCore.QSize(260, 560))
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowFlags(flags)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b = QtWidgets.QWidget(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), MainWindow.height()))
        self.b.setStyleSheet("background-color: rgba(0, 0, 0, 80%); border:1px; border-radius: 25px;")
        self.CloseButton = QtWidgets.QToolButton(self.centralwidget)
        self.CloseButton.setGeometry(210,0,50,25)
        self.CloseButton.setStyleSheet("font: 20px; background: red; border-width: 20px; border-top-left-radius: 10px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; border-top-right-radius:10px;")
        self.CloseButton.setObjectName("closeButton")
        self.CloseButton.clicked.connect(self.Close_Event)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(0, 51, 801, 121))
        self.line.setStyleSheet("border-top: 1px solid #b3b3b3;  ")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setEnabled(True)
        self.line_2.setGeometry(QtCore.QRect(0, 170, 811, 121))
        self.line_2.setStyleSheet("border-top: 1px solid #b3b3b3; border-bottom: 1px solid #b3b3b3")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setEnabled(True)
        self.line_11.setGeometry(QtCore.QRect(100, 60, 151, 41))
        self.line_11.setStyleSheet("border: 1px solid #b3b3b3;")
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setEnabled(True)
        self.line_3.setGeometry(QtCore.QRect(0, 290, 811, 121))
        self.line_3.setStyleSheet("border-top: 1px solid #b3b3b3; border-bottom: 1px solid #b3b3b3")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setEnabled(True)
        self.line_4.setGeometry(QtCore.QRect(0, 410, 811, 121))
        self.line_4.setStyleSheet("border-top: 1px solid #b3b3b3; border-bottom: 1px solid #b3b3b3")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setEnabled(True)
        self.line_12.setGeometry(QtCore.QRect(100, 120, 151, 41))
        self.line_12.setStyleSheet("border: 1px solid #b3b3b3;")
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setEnabled(True)
        self.line_13.setGeometry(QtCore.QRect(100, 180, 151, 41))
        self.line_13.setStyleSheet("border: 1px solid #b3b3b3;")
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setEnabled(True)
        self.line_14.setGeometry(QtCore.QRect(100, 240, 151, 41))
        self.line_14.setStyleSheet("border: 1px solid #b3b3b3;")
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setEnabled(True)
        self.line_15.setGeometry(QtCore.QRect(100, 300, 151, 41))
        self.line_15.setStyleSheet("border: 1px solid #b3b3b3;")
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setEnabled(True)
        self.line_16.setGeometry(QtCore.QRect(100, 360, 151, 41))
        self.line_16.setStyleSheet("border: 1px solid #b3b3b3;")
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setEnabled(True)
        self.line_17.setGeometry(QtCore.QRect(100, 420, 151, 41))
        self.line_17.setStyleSheet("border: 1px solid #b3b3b3;")
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setEnabled(True)
        self.line_18.setGeometry(QtCore.QRect(100, 480, 151, 41))
        self.line_18.setStyleSheet("border: 1px solid #b3b3b3;")
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_3.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.line_11.raise_()
        self.line_4.raise_()
        self.line_12.raise_()
        self.line_13.raise_()
        self.line_14.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        self.line_17.raise_()
        self.line_18.raise_()

        #----------------LOGO----------------
        self.label_BTC = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC.setGeometry(QtCore.QRect(10, 50, 81, 101))
        self.label_BTC.setObjectName("label_BTC")
        self.label_BTC.setPixmap(QtGui.QPixmap("Logo\BTC.webp"))

        self.label_ETH = QtWidgets.QLabel(self.centralwidget)
        self.label_ETH.setGeometry(QtCore.QRect(10, 180, 61, 81))
        self.label_ETH.setObjectName("label_ETH")
        self.label_ETH.setPixmap(QtGui.QPixmap("Logo\Ethereum_logo_2014.svg"))
        self.label_ETH.setScaledContents(True)

        self.label_GRIMM = QtWidgets.QLabel(self.centralwidget)
        self.label_GRIMM.setGeometry(QtCore.QRect(10, 300, 101, 81))
        self.label_GRIMM.setObjectName("label_GRIMM")
        self.label_GRIMM.setPixmap(QtGui.QPixmap("Logo\GRIMM.webp"))

        self.label_RVN = QtWidgets.QLabel(self.centralwidget)
        self.label_RVN.setGeometry(QtCore.QRect(-5, 420, 91, 81))
        self.label_RVN.setObjectName("label_RVN")
        self.label_RVN.setPixmap(QtGui.QPixmap("Logo/ravencoin-rvn-logo.png"))
        self.label_RVN.setScaledContents(True)

        self.label_BTC_NAME = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC_NAME.setGeometry(QtCore.QRect(10, 150, 101, 16))
        self.label_BTC_NAME.setObjectName("Logo\label_BTC_NAME")
        # ----------------LOGO----------------


        # ----------------NAME----------------
        self.label_BTC_NAME = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC_NAME.setGeometry(QtCore.QRect(10, 150, 101, 16))
        self.label_BTC_NAME.setObjectName("label_BTC_NAME")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_BTC_NAME.setFont(font)
        self.label_BTC_NAME.setStyleSheet("color: #fcfcfc;")

        self.label_ETH_NAME = QtWidgets.QLabel(self.centralwidget)
        self.label_ETH_NAME.setGeometry(QtCore.QRect(10, 270, 101, 16))
        self.label_ETH_NAME.setObjectName("label_ETH_NAME")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_ETH_NAME.setFont(font)
        self.label_ETH_NAME.setStyleSheet("color: #fcfcfc;")

        self.label_GRIMM_NAME = QtWidgets.QLabel(self.centralwidget)
        self.label_GRIMM_NAME.setGeometry(QtCore.QRect(10, 390, 101, 16))
        self.label_GRIMM_NAME.setObjectName("label_GRIMM_NAME")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_GRIMM_NAME.setFont(font)
        self.label_GRIMM_NAME.setStyleSheet("color: #fcfcfc;")

        self.label_RVN_NAME = QtWidgets.QLabel(self.centralwidget)
        self.label_RVN_NAME.setGeometry(QtCore.QRect(10, 510, 101, 16))
        self.label_RVN_NAME.setStyleSheet("color: #fcfcfc;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_RVN_NAME.setFont(font)
        self.label_RVN_NAME.setObjectName("label_RVN_NAME")
        # ----------------NAME----------------


        # ----------------VALUE----------------
        self.label_BTC_USD = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC_USD.setGeometry(QtCore.QRect(110, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_BTC_USD.setFont(font)
        self.label_BTC_USD.setStyleSheet("color: #fcfcfc;")
        self.label_BTC_USD.setObjectName("label_BTC_USD")

        self.label_BTC_RUB = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC_RUB.setGeometry(QtCore.QRect(110, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_BTC_RUB.setFont(font)
        self.label_BTC_RUB.setStyleSheet("color: #fcfcfc;")
        self.label_BTC_RUB.setObjectName("label_BTC_RUB")

        self.label_ETH_RUB = QtWidgets.QLabel(self.centralwidget)
        self.label_ETH_RUB.setGeometry(QtCore.QRect(110, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ETH_RUB.setFont(font)
        self.label_ETH_RUB.setStyleSheet("color: #fcfcfc;")
        self.label_ETH_RUB.setObjectName("label_ETH_RUB")

        self.label_ETH_USD = QtWidgets.QLabel(self.centralwidget)
        self.label_ETH_USD.setGeometry(QtCore.QRect(110, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ETH_USD.setFont(font)
        self.label_ETH_USD.setStyleSheet("color: #fcfcfc;")
        self.label_ETH_USD.setObjectName("label_ETHUSD")

        self.label_RVN_NOW = QtWidgets.QLabel(self.centralwidget)
        self.label_RVN_NOW.setGeometry(QtCore.QRect(110, 420, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_RVN_NOW.setFont(font)
        self.label_RVN_NOW.setStyleSheet("color: #fcfcfc;")
        self.label_RVN_NOW.setObjectName("label_RVN_NOW")

        self.label_RVN_HIGH = QtWidgets.QLabel(self.centralwidget)
        self.label_RVN_HIGH.setGeometry(QtCore.QRect(110, 480, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_RVN_HIGH.setFont(font)
        self.label_RVN_HIGH.setStyleSheet("color: #fcfcfc;")
        self.label_RVN_HIGH.setObjectName("label_RVN_HIGH")

        self.label_GR_NOW = QtWidgets.QLabel(self.centralwidget)
        self.label_GR_NOW.setGeometry(QtCore.QRect(110, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_GR_NOW.setFont(font)
        self.label_GR_NOW.setStyleSheet("color: #fcfcfc;")
        self.label_GR_NOW.setObjectName("label_GR_NOW")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(110, 360, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: #fcfcfc;")
        self.label_15.setObjectName("label_15")

        self.label_ETH_RUB.raise_()
        self.label_ETH_USD.raise_()
        self.label_BTC_RUB.raise_()
        self.label_BTC_USD.raise_()
        # ----------------VALUE----------------

        self.label_BTC_RUB_NOW_UP = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC_RUB_NOW_UP.setGeometry(QtCore.QRect(226, 60, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_BTC_RUB_NOW_UP.setFont(font)
        self.label_BTC_RUB_NOW_UP.setStyleSheet("color: #fcfcfc;")
        self.label_BTC_RUB_NOW_UP.setObjectName("label_BTC_RUB_NOW_UP")
        self.label_BTC_RUB_D = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC_RUB_D.setGeometry(QtCore.QRect(226, 85, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_BTC_RUB_D.setFont(font)
        self.label_BTC_RUB_D.setStyleSheet("color: #fcfcfc;")
        self.label_BTC_RUB_D.setObjectName("label_BTC_RUB_D")
        self.label_BTC_DL_D = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC_DL_D.setGeometry(QtCore.QRect(226, 145, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_BTC_DL_D.setFont(font)
        self.label_BTC_DL_D.setStyleSheet("color: #fcfcfc;")
        self.label_BTC_DL_D.setObjectName("label_BTC_DL_D")
        self.label_BTC_NOW_UP_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_BTC_NOW_UP_2.setGeometry(QtCore.QRect(226, 120, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_BTC_NOW_UP_2.setFont(font)
        self.label_BTC_NOW_UP_2.setStyleSheet("color: #fcfcfc;")
        self.label_BTC_NOW_UP_2.setObjectName("label_BTC_NOW_UP_2")
        self.label_ETH_RUB_D = QtWidgets.QLabel(self.centralwidget)
        self.label_ETH_RUB_D.setGeometry(QtCore.QRect(226, 205, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ETH_RUB_D.setFont(font)
        self.label_ETH_RUB_D.setStyleSheet("color: #fcfcfc;")
        self.label_ETH_RUB_D.setObjectName("label_ETH_RUB_D")
        self.label_ETH_RUB_UP = QtWidgets.QLabel(self.centralwidget)
        self.label_ETH_RUB_UP.setGeometry(QtCore.QRect(226, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_ETH_RUB_UP.setFont(font)
        self.label_ETH_RUB_UP.setStyleSheet("color: #fcfcfc;")
        self.label_ETH_RUB_UP.setObjectName("label_ETH_RUB_UP")
        self.label_ETH_DL_D = QtWidgets.QLabel(self.centralwidget)
        self.label_ETH_DL_D.setGeometry(QtCore.QRect(226, 265, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ETH_DL_D.setFont(font)
        self.label_ETH_DL_D.setStyleSheet("color: #fcfcfc;")
        self.label_ETH_DL_D.setObjectName("label_ETH_DL_D")
        self.label_ETH_DL_NOW_UP = QtWidgets.QLabel(self.centralwidget)
        self.label_ETH_DL_NOW_UP.setGeometry(QtCore.QRect(226, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_ETH_DL_NOW_UP.setFont(font)
        self.label_ETH_DL_NOW_UP.setStyleSheet("color: #fcfcfc;")
        self.label_ETH_DL_NOW_UP.setObjectName("label_ETH_DL_NOW_UP")
        self.label_GRIMM_BTC_NOW_D = QtWidgets.QLabel(self.centralwidget)
        self.label_GRIMM_BTC_NOW_D.setGeometry(QtCore.QRect(226, 325, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_GRIMM_BTC_NOW_D.setFont(font)
        self.label_GRIMM_BTC_NOW_D.setStyleSheet("color: #fcfcfc;")
        self.label_GRIMM_BTC_NOW_D.setObjectName("label_GRIMM_BTC_NOW_D")
        self.label_GRIMM_BTC_NOW_UP = QtWidgets.QLabel(self.centralwidget)
        self.label_GRIMM_BTC_NOW_UP.setGeometry(QtCore.QRect(226, 300, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_GRIMM_BTC_NOW_UP.setFont(font)
        self.label_GRIMM_BTC_NOW_UP.setStyleSheet("color: #fcfcfc;")
        self.label_GRIMM_BTC_NOW_UP.setObjectName("label_GRIMM_BTC_NOW_UP")
        self.label_GRIMM_BTC_HIGH_D = QtWidgets.QLabel(self.centralwidget)
        self.label_GRIMM_BTC_HIGH_D.setGeometry(QtCore.QRect(226, 385, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_GRIMM_BTC_HIGH_D.setFont(font)
        self.label_GRIMM_BTC_HIGH_D.setStyleSheet("color: #fcfcfc;")
        self.label_GRIMM_BTC_HIGH_D.setObjectName("label_GRIMM_BTC_HIGH_D")
        self.label_GRIMM_BTC_HIGH_UP = QtWidgets.QLabel(self.centralwidget)
        self.label_GRIMM_BTC_HIGH_UP.setGeometry(QtCore.QRect(226, 360, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_GRIMM_BTC_HIGH_UP.setFont(font)
        self.label_GRIMM_BTC_HIGH_UP.setStyleSheet("color: #fcfcfc;")
        self.label_GRIMM_BTC_HIGH_UP.setObjectName("label_GRIMM_BTC_HIGH_UP")
        self.label_RVN_BTC_NOW_D = QtWidgets.QLabel(self.centralwidget)
        self.label_RVN_BTC_NOW_D.setGeometry(QtCore.QRect(226, 445, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_RVN_BTC_NOW_D.setFont(font)
        self.label_RVN_BTC_NOW_D.setStyleSheet("color: #fcfcfc;")
        self.label_RVN_BTC_NOW_D.setObjectName("label_RVN_BTC_NOW_D")
        self.label_RVN_BTC_NOW_UP = QtWidgets.QLabel(self.centralwidget)
        self.label_RVN_BTC_NOW_UP.setGeometry(QtCore.QRect(226, 420, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_RVN_BTC_NOW_UP.setFont(font)
        self.label_RVN_BTC_NOW_UP.setStyleSheet("color: #fcfcfc;")
        self.label_RVN_BTC_NOW_UP.setObjectName("label_RVN_BTC_NOW_UP")
        self.label_RVN_BTC_HIGH_D = QtWidgets.QLabel(self.centralwidget)
        self.label_RVN_BTC_HIGH_D.setGeometry(QtCore.QRect(226, 505, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_RVN_BTC_HIGH_D.setFont(font)
        self.label_RVN_BTC_HIGH_D.setStyleSheet("color: #fcfcfc;")
        self.label_RVN_BTC_HIGH_D.setObjectName("label_RVN_BTC_HIGH_D")
        self.label_RVN_BTC_HIGH_UP = QtWidgets.QLabel(self.centralwidget)
        self.label_RVN_BTC_HIGH_UP.setGeometry(QtCore.QRect(226, 480, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_RVN_BTC_HIGH_UP.setFont(font)
        self.label_RVN_BTC_HIGH_UP.setStyleSheet("color: #fcfcfc;")
        self.label_RVN_BTC_HIGH_UP.setObjectName("label_RVN_BTC_HIGH_UP")

        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Криптовалютный парсер"))
        self.CloseButton.setText(_translate("MainWindow","X"))
        self.label_BTC_NAME.setText(_translate("MainWindow", "Bitcoin"))
        self.label_ETH_NAME.setText(_translate("MainWindow", "Etherium"))
        self.label_GRIMM_NAME.setText(_translate("MainWindow", "Grimm"))
        self.label_RVN_NAME.setText(_translate("MainWindow", "Raven"))
        self.label_BTC_RUB_NOW_UP.setText(_translate("MainWindow", "CUR"))
        self.label_BTC_RUB_D.setText(_translate("MainWindow", "RUB"))
        self.label_BTC_DL_D.setText(_translate("MainWindow", "USD"))
        self.label_BTC_NOW_UP_2.setText(_translate("MainWindow", "CUR"))
        self.label_ETH_RUB_D.setText(_translate("MainWindow", "RUB"))
        self.label_ETH_RUB_UP.setText(_translate("MainWindow", "CUR"))
        self.label_ETH_DL_D.setText(_translate("MainWindow", "USD"))
        self.label_ETH_DL_NOW_UP.setText(_translate("MainWindow", "CUR"))
        self.label_GRIMM_BTC_NOW_D.setText(_translate("MainWindow", "BTC"))
        self.label_GRIMM_BTC_NOW_UP.setText(_translate("MainWindow", "CUR"))
        self.label_GRIMM_BTC_HIGH_D.setText(_translate("MainWindow", "BTC"))
        self.label_GRIMM_BTC_HIGH_UP.setText(_translate("MainWindow", "HIG"))
        self.label_RVN_BTC_NOW_D.setText(_translate("MainWindow", "BTC"))
        self.label_RVN_BTC_NOW_UP.setText(_translate("MainWindow", "CUR"))
        self.label_RVN_BTC_HIGH_D.setText(_translate("MainWindow", "BTC"))
        self.label_RVN_BTC_HIGH_UP.setText(_translate("MainWindow", "HIG"))

    def setText(self):
        self.TextEd = DataThread()
        self.TextEd.setText.connect(self.TextToEditor)
        self.TextEd.start()

    def TextToEditor(self, text, value):
        if(text == "BTC-RUB"):
            self.label_BTC_RUB.setText(value)
        elif (text == "BTC-USD"):
            self.label_BTC_USD.setText(value)
        elif (text == "ETH-RUB"):
            self.label_ETH_RUB.setText(value)
        elif (text == "ETH-USD"):
            self.label_ETH_USD.setText(value)
        elif (text == "Grimm"):
            list = value.split(';')
            self.label_GR_NOW.setText(list[0])
            self.label_15.setText(list[1])
        elif (text == "Raven"):
            list = value.split(';')
            self.label_RVN_NOW.setText(list[0])
            self.label_RVN_HIGH.setText(list[1])

    def Close_Event(self):
        sys.exit()



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QtGui.QIcon("Logo\CP.png"))
        self.setText()
        self._old_pos = None
        self.OnTopCheck = 0
        self.OnTopButton = QtWidgets.QPushButton(self.centralwidget)
        self.OnTopButton.setGeometry(0, 0, 50, 25)
        self.OnTopButton.setObjectName("OnTopButton")
        self.OnTopButton.setText('Поверх \nОкон')
        self.OnTopButton.setStyleSheet("font: 11px; background: red; border-width: 20px; border-top-left-radius: 10px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; border-top-right-radius:10px;")
        self.OnTopButton.clicked.connect(self.StaysOnTopHint)

    def StaysOnTopHint(self):
        if(self.OnTopCheck == 0):
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
            self.OnTopCheck = 1
            self.OnTopButton.setStyleSheet("font: 11px; background: green;; border-width: 20px; border-top-left-radius: 10px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; border-top-right-radius:10px;")
        else:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.OnTopCheck = 0
            self.OnTopButton.setStyleSheet("font: 11px; background: red; border-width: 20px; border-top-left-radius: 10px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; border-top-right-radius:10px;")
        self.show()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = MainWindow()
    # ui.setupUi(MainWindow)
    # ui.show()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
