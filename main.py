import requests as req
import json
from tkinter import *

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
window = Tk()
window.geometry('400x250')
window.configure(background="#262525")
lb = Label(text='Hello')

lb.pack(side=TOP)

window.mainloop()
