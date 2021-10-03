import requests as req
import json
from tkinter import *
import tkinter.ttk as ttk

path_for_coinbase = 'CoinBase.json'
path_for_tradeogre = 'TradeOgre.json'


def get_price_from_coinbase():
    with open(path_for_coinbase, 'r') as f:
        data = json.loads(f.read())
        for value in data:
            resp = req.get(data[value]).json()
            price = float(resp.get('data').get('amount'))
            if resp.get('data').get('currency') == 'RUB':
                print('Стоимость валюты {}: {}'.format(value, "{:,.0f}".format(price)), 'рублей')
            elif resp.get('data').get('currency') == 'USD':
                print('Стоимость валюты {}: {}'.format(value, "{:,.0f}".format(price)), 'долларов')
            else:
                print('Нет такой валюты)')

            # "{:,.0f}".format(price)
            # {:[количество_символов][запятая][.число_знаков_в_дробной_части] плейсхолдер}


def get_price_from_tradeogre():
    with open(path_for_tradeogre, 'r') as f:
        data = json.loads(f.read())
        for value in data:
            resp = req.get(data[value]).json()
            price = resp.get('price')
            print('Стоимость валюты {} в биткоинах: {}'.format(value, price))


# Окно
lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))

window = Tk()
window.geometry('400x250')
window.configure(bg="#262525")
window.overrideredirect(1)
window.resizable(False,False)
window.attributes('-topmost', True)
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)
close = Button(window,text = "Close",command=window.destroy)
close.grid(padx=359,pady=1)
#lb = Label(text='Hello')
#lb.pack(side=TOP)
window.mainloop()
