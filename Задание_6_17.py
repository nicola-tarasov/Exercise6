"""
///////////////////////////////////////////////////
ЗАДАНИЕ 6
////////////////////////////////////////////////////
Выполнено на основе скрипта "Задание_5_6.py".
Курс обучения: "АЦ. Программирование на языке Python
от базового уровня до продвинутого_1"
Преподаватель: Голиков Денис Владимирович
Слушатель: Тарасов Николай Александрович
Группа: ППБУ-1.1
/////////////////////////////////////////////////////////////////
1. Создайте приложение с графическим интерфейсом на языке Python,
   которое будет отображать текущие курсы
   популярных криптовалют к доллару США,
   используя данные открытого API CoinGecko
   (см. https://www.coingecko.com/en/api).
2. При выполнении домашнего задания используйте Git и
   сделайте не менее трех коммитов.
3. Оформите техническое задание на разработку этого приложения.
   Не забудьте добавить в него эскиз интерфейса.
////////////////////////////////////////////////////////////////////
//                       Решение задания 6                        //
//            Создан на основе скрипта Задание_5_6.py             //
//   Функционал:                                                  //
//  запрос обменных курсов покупки и продажи валют (Asc и Bid);  //
//  расчёт относительного отклонения в промилле (‰Spread);       //
//  доступны котировки крипты, фиатов, синтетиков и металлов;    //
//  расчёт четырёх валют (основной, платежа и двух обменных);    //
//  валюты выбираются из списка или путём ввода буквенных кодов. //
////////////////////////////////////////////////////////////////////
"""


from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json
from datetime import datetime, timezone
# from datetime import timedelta


def update_base0_currency_symbol(event):
    global currencies
    # Считываем имя валюты из комбобокса
    name = base0_combobox.get()
    symbol = currencies[name]
    base0_currency_symbol.config(text=symbol)
    print(f" {symbol}: {name}")


def update_base1_currency_symbol(event):
    global currencies
    # Считываем имя валюты из комбобокса
    name = base1_combobox.get()
    symbol = currencies[name]
    base1_currency_symbol.config(text=symbol)
    print(f" {symbol}: {name}")


def update_base2_currency_symbol(event):
    global currencies
    # Считываем имя валюты из комбобокса
    name = base2_combobox.get()
    symbol = currencies[name]
    base2_currency_symbol.config(text=symbol)
    print(f" {symbol}: {name}")


def exchange_rates():
    global currencies
    # Считываем наименования валют
    base__name = "Биткойн (крипта): BTC"  # Имя из Coingecko-словаря валют. Проверь!
    base0_name = base0_combobox.get()
    base1_name = base1_combobox.get()
    base2_name = base2_combobox.get()

    # Уточняем символ валют
    if base__name in currencies:
        base__symbol = currencies[base__name]
    else:
        base__symbol = 'btc'  # Код основной валюты. Подстраховка на любой случай!
        base__symbol = base__symbol.lower()  # Преобразование в строчные буквы
    #
    if base0_name in currencies:
        base0_symbol = currencies[base0_name]
    else:
        base0_symbol = base0_name
        base0_symbol = base0_symbol.lower()  # Преобразование в строчные буквы
    base0_currency_symbol.config(text=base0_symbol)
    #
    if base1_name in currencies:
        base1_symbol = currencies[base1_name]
    else:
        base1_symbol = base1_name
        base1_symbol = base1_symbol.lower()  # Преобразование в строчные буквы
    base1_currency_symbol.config(text=base1_symbol)
    #
    if base2_name in currencies:
        base2_symbol = currencies[base2_name]
    else:
        base2_symbol = base2_name
        base2_symbol = base2_symbol.lower()  # Преобразование в строчные буквы
    base2_currency_symbol.config(text=base2_symbol)

    print(f'УСЛОВИЯ ЗАПРОСА')
    print(f" Основная  валюта: {base__symbol}: {base__name}")
    print(f" Платёжная валюта: {base0_symbol}: {base0_name}")
    print(f" Обменная валюта1: {base1_symbol}: {base1_name}")
    print(f" Обменная валюта2: {base2_symbol}: {base2_name}")

    if base__symbol and base0_symbol and base1_symbol and base2_symbol:
        try:
            # Источник1
            # Запросить курсы обмена BTC на другие валюты.
            # Одним списком доступно 95 обменных курсов биткоина (14 крипт, 1 синтетик, 78 фиатов, 2 метала):
            url1 = "https://api.coingecko.com/api/v3/exchange_rates"
            print(f"Источник1: {url1}")
            time1_1 = datetime.now(timezone.utc)  # Момент UTC-времени перед запросом1
            print(f"Момент UTC-времени1_1: {time1_1}")
            response1 = requests.get(url1) # Запросить курсы обмена BTC на другие валюты.
            time1_2 = datetime.now(timezone.utc)  # Момент UTC-времени после запроса1
            print(f"Момент UTC-времени1_2: {time1_2}")
            d_time1 = time1_2 - time1_1  # Продолжительность запроса1
            print(f"Длительность запроса1: {d_time1}")
            #
            # url = "https://api.coingecko.com/api/v3/exchange_rates"  # Запросить курсы обмена BTC на другие валюты.
            # {
            #   "rates": {
            #     "btc": {
            #       "name": "Bitcoin",
            #       "unit": "BTC",
            #       "value": 1.0,
            #       "type": "crypto"
            #     },
            #     "eth": {
            #       "name": "Ether",
            #       "unit": "ETH",
            #       "value": 34.292,
            #       "type": "crypto"
            #     },
            #     "ltc": {
            #       "name": "Litecoin",
            #       "unit": "LTC",
            #       "value": 1383.402,
            #       "type": "crypto"
            #     },
            #
            #
            response1.raise_for_status()  # Метод из библиотеки requests в Python.
            # Он проверяет статус-код ответа HTTP и вызывает исключение HTTPError
            # при ошибках клиента (4xx) или сервера (5xx).
            # Если запрос успешен (код в диапазоне 200–299),
            # метод ничего не делает и просто возвращает управление.
            #
            data1 = response1.json()  # Метод из библиотеки Requests,
            # который позволяет автоматически преобразовать тело HTTP-ответа (в формате JSON)
            # в структуру данных Python (например, словарь или список).
            # Это значительно упрощает работу с API,
            # так как избавляет от необходимости вручную парсить JSON-строку.
            #
            # print('Печать HTTP-ответа1 без форматирования:')
            # print(data1)  # Данные обменных курсов относительно базовой валюты_ в формате JSON.
            #
            # print('Печать HTTP-ответа1 с форматированием:')
            # print(json.dumps(data1, indent=2))

            # print(data1['rates'])
            # print(data1['rates'][base__symbol])
            # print(data1['rates'][base0_symbol])
            # print(data1['rates'][base1_symbol])
            # print(data1['rates'][base2_symbol])
            # if ((base__symbol in data1['rates'] and base0_symbol in data1['rates']) and
            #     (base1_symbol in data1['rates'] and base2_symbol in data1['rates'])):

            if base__symbol in data1['rates']:
                data1_base__vs_base_ = data1['rates'][base__symbol]['value']
                data1_base__exchange_rate = (float(data1['rates'][base0_symbol]['value']) /
                                             float(data1_base__vs_base_))
                print(f" 1 {base__symbol} ⇄ {data1_base__vs_base_} {base__symbol}")
            else:
                data1_base__vs_base_ = float(0)
                data1_base__exchange_rate = float(0)
                print(f"Основная валюта {base__symbol}: {base__name} в источнике1 не найдена")
                print(f" 1 {base__symbol} ⇄ {data1_base__vs_base_} {base__symbol}")
            #     mb.showerror("Ошибка", f"Основная валюта {base__symbol}: {base__name} в источнике1 не найдена")

            if base0_symbol in data1['rates']:
                data1_base__vs_base0 = data1['rates'][base0_symbol]['value']
                data1_base0_exchange_rate = (float(data1['rates'][base0_symbol]['value']) /
                                             float(data1_base__vs_base0))
                print(f" 1 {base__symbol} ⇄ {data1_base__vs_base0} {base0_symbol}")
            else:
                data1_base__vs_base0 = float(0)
                data1_base0_exchange_rate = float(0)
                print(f"Платёжная валюта {base0_symbol}: {base0_name} в источнике1 не найдена")
                print(f" 1 {base__symbol} ⇄ {data1_base__vs_base0} {base0_symbol}")
            #     mb.showerror("Ошибка", f"Платёжная валюта {base0_symbol}: {base0_name} в источнике1 не найдена")

            if base1_symbol in data1['rates']:
                data1_base__vs_base1 = data1['rates'][base1_symbol]['value']
                data1_base1_exchange_rate = (float(data1['rates'][base0_symbol]['value']) /
                                             float(data1_base__vs_base1))
                print(f" 1 {base__symbol} ⇄ {data1_base__vs_base1} {base1_symbol}")
            else:
                data1_base__vs_base1 = float(0)
                data1_base1_exchange_rate = float(0)
                print(f"Обменная валюта1 {base1_symbol}: {base1_name} в источнике1 не найдена")
                print(f" 1 {base__symbol} ⇄ {data1_base__vs_base1} {base1_symbol}")
            #     mb.showerror("Ошибка", f"Обменная валюта1 {base1_symbol}: {base1_name} в источнике1 не найдена")

            if base2_symbol in data1['rates']:
                data1_base__vs_base2 = data1['rates'][base2_symbol]['value']
                data1_base2_exchange_rate = (float(data1['rates'][base0_symbol]['value']) /
                                             float(data1_base__vs_base2))
                print(f" 1 {base__symbol} ⇄ {data1_base__vs_base2} {base2_symbol}")
            else:
                data1_base__vs_base2 = float(0)
                data1_base2_exchange_rate = float(0)
                print(f"Обменная валюта2 {base2_symbol}: {base2_name} в источнике1 не найдена")
                print(f" 1 {base__symbol} ⇄ {data1_base__vs_base2} {base2_symbol}")
            #     mb.showerror("Ошибка", f"Обменная валюта2 {base2_symbol}: {base2_name} в источнике1 не найдена")

                # print(f'Текущие ставки1:')
                # print(f"{base__symbol}: {base__name}")
                # print(f" 1 {base__symbol} ⇄ {data1_base__vs_base_:.6E} {base__symbol}")
                # print(f" 1 {base__symbol} ⇄ {data1_base__vs_base0:.6E} {base0_symbol}")
                # print(f" 1 {base__symbol} ⇄ {data1_base__vs_base1:.6E} {base1_symbol}")
                # print(f" 1 {base__symbol} ⇄ {data1_base__vs_base2:.6E} {base2_symbol}")
                # print(f"datetime1: {d_time1}")
                #
                # mb.showinfo("Курсы обмена1", (f"Текущие ставки1: \n"
                #                               f" 1 {base__symbol} ⇄ {data1_base__exchange_rate:.6E} {base0_symbol}\n"
                #                               f" 1 {base0_symbol} ⇄ {data1_base0_exchange_rate:.6E} {base0_symbol}\n"
                #                               f" 1 {base1_symbol} ⇄ {data1_base1_exchange_rate:.6E} {base0_symbol}\n"
                #                               f" 1 {base2_symbol} ⇄ {data1_base2_exchange_rate:.6E} {base0_symbol}\n"
                #                               f"По данным: {url1}\n"
                #                               f"На момент UTC-времени1: {d_time1}\n"
                #                               f""))



            # Источник2
            # Запросить курсы обмена BTC на заданные валюты.
            url2 = (f"https://api.coingecko.com/api/v3/simple/price?"
                    # f"symbols={base__symbol},{base0_symbol},{base1_symbol},{base2_symbol}&"
                    f"symbols={base__symbol}&"
                    f"vs_currencies={base__symbol},{base0_symbol},{base1_symbol},{base2_symbol}")
            # {
            #   "btc": {
            #     "usd": 77609,
            #     "eur": 69309,
            #     "rub": 6338598,
            #     "bgn": 135554,
            #     "svc": 679240,
            #     "xdr": 56881
            #   },
            headers = {
                "accept": "application/json",
                "x_cg_demo_api_key": "CG-maxq2WzQMeR4ccuoJ5BQWL53"  # Индивидуальный ключ доступа
            }

            print(f"Источник2: {url2}")
            time2_1 = datetime.now(timezone.utc)  # Момент UTC-времени перед запросом2
            print(f"Момент UTC-времени2_1: {time2_1}")
            response2 = requests.get(url2, headers=headers)
            time2_2 = datetime.now(timezone.utc)  # Момент UTC-времени после запроса2
            print(f"Момент UTC-времени2_2: {time2_2}")
            d_time2 = time2_2 - time2_1  # Продолжительность запроса2
            print(f"Длительность запроса2: {d_time2}")
            d_time = d_time1 + d_time2  # Продолжительность запроса 1 и 2
            print(f"Длительность запросов: {d_time}")

            # Одним списком доступно 16 обменных курса
            # между всеми 4-мя заданными валютами (4x4)
            response2.raise_for_status()  # Метод из библиотеки requests в Python.
            # Он проверяет статус-код ответа HTTP и вызывает исключение HTTPError
            # при ошибках клиента (4xx) или сервера (5xx).
            # Если запрос успешен (код в диапазоне 200–299),
            # метод ничего не делает и просто возвращает управление.
            #
            data2 = response2.json()  # Метод из библиотеки Requests,
            # который позволяет автоматически преобразовать тело HTTP-ответа (в формате JSON)
            # в структуру данных Python (например, словарь или список).
            # Это значительно упрощает работу с API,
            # так как избавляет от необходимости вручную парсить JSON-строку.
            #
            # print('Печать HTTP-ответа2 без форматирования:')
            # print(data2)  # Данные обменных курсов относительно базовой валюты_ в формате JSON.
            #
            # print('Печать HTTP-ответа2 с форматированием:')
            # print(json.dumps(data2, indent=2))

            # print(data2[base__symbol])
            # print(data2[base__symbol][base__symbol])
            # print(data2[base__symbol][base0_symbol])
            # print(data2[base__symbol][base1_symbol])
            # print(data2[base__symbol][base2_symbol])
            # print(base__symbol in data2[base__symbol])
            # print(base0_symbol in data2[base__symbol])
            # print(base1_symbol in data2[base__symbol])
            # print(base2_symbol in data2[base__symbol])
            # if ((base__symbol in data2[base__symbol] and base0_symbol in data2[base__symbol]) and
            #         (base1_symbol in data2[base__symbol] and base2_symbol in data2[base__symbol])):

            if base__symbol in data2[base__symbol]:
                data2_base__vs_base_ = data2[base__symbol][base__symbol]
                data2_base__exchange_rate = (float(data2[base__symbol][base0_symbol]) /
                                             float(data2_base__vs_base_))
                print(f" 1 {base__symbol} ⇄ {data2_base__vs_base_} {base__symbol}")
            else:
                data2_base__vs_base_ = float(0)
                data2_base__exchange_rate = float(0)
                print(f"Основная валюта {base__symbol}: {base__name} в источнике2 не найдена")
                print(f" 1 {base__symbol} ⇄ {data2_base__vs_base_} {base__symbol}")
            #     mb.showerror("Ошибка", f"Основная валюта {base__symbol}: {base__name} в источнике2 не найдена")

            if base0_symbol in data2[base__symbol]:
                data2_base__vs_base0 = data2[base__symbol][base0_symbol]
                data2_base0_exchange_rate = (float(data2[base__symbol][base0_symbol]) /
                                             float(data2_base__vs_base0))
                print(f" 1 {base__symbol} ⇄ {data2_base__vs_base0} {base0_symbol}")
            else:
                data2_base__vs_base0 = float(0)
                data2_base0_exchange_rate = float(0)
                print(f"Платёжная валюта {base0_symbol}: {base0_name} в источнике2 не найдена")
                print(f" 1 {base__symbol} ⇄ {data2_base__vs_base0} {base0_symbol}")
            #     mb.showerror("Ошибка", f"Платёжная валюта {base0_symbol}: {base0_name} в источнике2 не найдена")

            if base1_symbol in data2[base__symbol]:
                data2_base__vs_base1 = data2[base__symbol][base1_symbol]
                data2_base1_exchange_rate = (float(data2[base__symbol][base0_symbol]) /
                                             float(data2_base__vs_base1))
                print(f" 1 {base__symbol} ⇄ {data2_base__vs_base1} {base1_symbol}")
            else:
                data2_base__vs_base1 = float(0)
                data2_base1_exchange_rate = float(0)
                print(f"Обменная валюта1 {base1_symbol}: {base1_name} в источнике2 не найдена")
                print(f" 1 {base__symbol} ⇄ {data2_base__vs_base1} {base1_symbol}")
            #     mb.showerror("Ошибка", f"Обменная валюта1 {base1_symbol}: {base1_name} в источнике2 не найдена")

            if base2_symbol in data2[base__symbol]:
                data2_base__vs_base2 = data2[base__symbol][base2_symbol]
                data2_base2_exchange_rate = (float(data2[base__symbol][base0_symbol]) /
                                             float(data2_base__vs_base2))
                print(f" 1 {base__symbol} ⇄ {data2_base__vs_base2} {base2_symbol}")
            else:
                data2_base__vs_base2 = float(0)
                data2_base2_exchange_rate = float(0)
                print(f"Обменная валюта2 {base2_symbol}: {base2_name} в источнике2 не найдена")
                print(f" 1 {base__symbol} ⇄ {data2_base__vs_base2} {base2_symbol}")
            #     mb.showerror("Ошибка", f"Обменная валюта2 {base2_symbol}: {base1_name} в источнике2 не найдена")

                # print(f'Текущие ставки2:')
                # print(f"{base__symbol}: {base__name}")
                # print(f" 1 {base__symbol} ⇄ {data2_base__vs_base_:.6E} {base__symbol}")
                # print(f" 1 {base__symbol} ⇄ {data2_base__vs_base0:.6E} {base0_symbol}")
                # print(f" 1 {base__symbol} ⇄ {data2_base__vs_base1:.6E} {base1_symbol}")
                # print(f" 1 {base__symbol} ⇄ {data2_base__vs_base2:.6E} {base2_symbol}")
                # print(f"datetime2: {d_time2}")
                #
                # mb.showinfo("Курсы обмена2", (f"Текущие ставки2: \n"
                #                               f" 1 {base__symbol} ⇄ {data2_base__exchange_rate:.6E} {base0_symbol};\n"
                #                               f" 1 {base0_symbol} ⇄ {data2_base0_exchange_rate:.6E} {base0_symbol};\n"
                #                               f" 1 {base1_symbol} ⇄ {data2_base1_exchange_rate:.6E} {base0_symbol};\n"
                #                               f" 1 {base2_symbol} ⇄ {data2_base2_exchange_rate:.6E} {base0_symbol}.\n"
                #                               f"По данным: {url2}\n"
                #                               f"На момент UTC-времени2: {d_time2}\n"
                #                               f")"))
            #     mb.showerror("Ошибка", f"Обменная валюта2 {base2_symbol}: {base2_name} в источнике2 не найдена")


            # //////////////////////////////////////////
            # Финал. Сравнение данных из двух источников
            # //////////////////////////////////////////

            # Спред между котировками из источника 1 и 2
            if data1_base__exchange_rate == data2_base__exchange_rate:
                base__exchange_rate_spread = 0
            else:
                base__exchange_rate_spread = -1000 * ((min(data1_base__exchange_rate, data2_base__exchange_rate) /
                                                       max(data1_base__exchange_rate, data2_base__exchange_rate)) - 1)
            print(f'base__exchange_rate_spread: {base__exchange_rate_spread}')

            if data1_base0_exchange_rate == data2_base0_exchange_rate:
                base0_exchange_rate_spread = 0
            else:
                base0_exchange_rate_spread = -1000 * ((min(data1_base0_exchange_rate, data2_base0_exchange_rate) /
                                                          max(data1_base0_exchange_rate, data2_base0_exchange_rate)) - 1)
            print(f'base0_exchange_rate_spread: {base0_exchange_rate_spread}')

            if data1_base1_exchange_rate == data2_base1_exchange_rate:
                base1_exchange_rate_spread = 0
            else:
                base1_exchange_rate_spread = -1000 * ((min(data1_base1_exchange_rate, data2_base1_exchange_rate) /
                                                          max(data1_base1_exchange_rate, data2_base1_exchange_rate)) - 1)
            print(f'base1_exchange_rate_spread: {base1_exchange_rate_spread}')

            if data1_base2_exchange_rate == data2_base2_exchange_rate:
                base2_exchange_rate_spread = 0
            else:
                base2_exchange_rate_spread = -1000 * ((min(data1_base2_exchange_rate, data2_base2_exchange_rate) /
                                                           max(data1_base2_exchange_rate, data2_base2_exchange_rate)) - 1)
            print(f'base2_exchange_rate_spread: {base2_exchange_rate_spread}')
            #
            # Символ отклонения базовых котировкок из источника 1 и 2 ("+/-" и "-/+" или "±" и "∓")
            if data1_base1_exchange_rate == data2_base1_exchange_rate:
                base__exchange_rate_deviations = ""
            elif data1_base__exchange_rate > data2_base__exchange_rate:
                base__exchange_rate_deviations = "+"
            elif data1_base__exchange_rate < data2_base__exchange_rate:
                base__exchange_rate_deviations = "-"

            if data1_base0_exchange_rate == data2_base0_exchange_rate:
                base0_exchange_rate_deviations = ""
            elif data1_base0_exchange_rate > data2_base0_exchange_rate:
                base0_exchange_rate_deviations = "+"
            elif data1_base0_exchange_rate < data2_base0_exchange_rate:
                base0_exchange_rate_deviations = "-"

            if data1_base1_exchange_rate == data2_base1_exchange_rate:
                base1_exchange_rate_deviations = ""
            elif data1_base1_exchange_rate > data2_base1_exchange_rate:
                base1_exchange_rate_deviations = "+"
            elif data1_base1_exchange_rate < data2_base1_exchange_rate:
                base1_exchange_rate_deviations = "-"

            if data1_base2_exchange_rate == data2_base2_exchange_rate:
                base2_exchange_rate_deviations = ""
            elif data1_base2_exchange_rate > data2_base2_exchange_rate:
                base2_exchange_rate_deviations = "+"
            elif data1_base2_exchange_rate < data2_base2_exchange_rate:
                base2_exchange_rate_deviations = "-"

            # Спред между котировками из источника 1 и 2

            if data1_base__vs_base_ == data2_base__vs_base_:
                base__vs_base__spread = 0
            else:
                base__vs_base__spread = -1000 * ((min(data1_base__vs_base_, data2_base__vs_base_) /
                                                     max(data1_base__vs_base_, data2_base__vs_base_)) - 1)
            print(f'base__vs_base__spread: {base__vs_base__spread}')

            if data1_base__vs_base0 == data2_base__vs_base0:
                base__vs_base0_spread = 0
            else:
                base__vs_base0_spread = -1000 * ((min(data1_base__vs_base0, data2_base__vs_base0) /
                                                     max(data1_base__vs_base0, data2_base__vs_base0)) - 1)
            print(f'base__vs_base0_spread: {base__vs_base0_spread}')

            if data1_base__vs_base1 == data2_base__vs_base1:
                base__vs_base1_spread = 0
            else:
                base__vs_base1_spread = -1000 * ((min(data1_base__vs_base1, data2_base__vs_base1) /
                                                     max(data1_base__vs_base1, data2_base__vs_base1)) - 1)
            print(f'base__vs_base1_spread: {base__vs_base1_spread}')

            if data1_base__vs_base2 == data2_base__vs_base2:
                base__vs_base2_spread = 0
            else:
                base__vs_base2_spread = -1000 * ((min(data1_base__vs_base2, data2_base__vs_base2) /
                                                     max(data1_base__vs_base2, data2_base__vs_base2)) - 1)
            print(f'base__vs_base2_spread: {base__vs_base2_spread}')
            #
            # Символ отклонения базовых котировкок из источника 1 и 2 ("+/-" и "-/+" или "±" и "∓")
            if data1_base__vs_base_ == data2_base__vs_base_:
                base__vs_base__deviations = ""
            elif data1_base__vs_base_ > data2_base__vs_base_:
                base__vs_base__deviations = "+"
            elif data1_base__vs_base_ < data2_base__vs_base_:
                base__vs_base__deviations = "-"

            if data1_base__vs_base0 == data2_base__vs_base0:
                base__vs_base0_deviations = ""
            elif data1_base__vs_base0 > data2_base__vs_base0:
                base__vs_base0_deviations = "+"
            elif data1_base__vs_base0 < data2_base__vs_base0:
                base__vs_base0_deviations = "-"

            if data1_base__vs_base1 == data2_base__vs_base1:
                base__vs_base1_deviations = ""
            elif data1_base__vs_base1 > data2_base__vs_base1:
                base__vs_base1_deviations = "+"
            elif data1_base__vs_base1 < data2_base__vs_base1:
                base__vs_base1_deviations = "-"

            if data1_base__vs_base2 == data2_base__vs_base2:
                base__vs_base2_deviations = ""
            elif data1_base__vs_base2 > data2_base__vs_base2:
                base__vs_base2_deviations = "+"
            elif data1_base__vs_base2 < data2_base__vs_base2:
                base__vs_base2_deviations = "-"


            #
            print(f'Текущие цены покупки / продажи валюты из источника 1 и 2, включая спред:')
            print(f"{base__symbol}: {base__name}")
            print(f" 1 {base__symbol} ⇄ {data1_base__vs_base_:.6E} / {data2_base__vs_base_:.6E} {base__symbol}"
                  f" ({base__vs_base__deviations}{base__vs_base__spread:.6f} ‰)")

            print(f" 1 {base__symbol} ⇄ {data1_base__vs_base0:.6E} / {data2_base__vs_base0:.6E} {base0_symbol}"
                  f" ({base__vs_base0_deviations}{base__vs_base0_spread:.6f} ‰)")

            print(f" 1 {base__symbol} ⇄ {data1_base__vs_base1:.6E} / {data2_base__vs_base1:.6E} {base1_symbol}"
                  f" ({base__vs_base1_deviations}{base__vs_base1_spread:.6f} ‰)")

            print(f" 1 {base__symbol} ⇄ {data1_base__vs_base2:.6E} / {data2_base__vs_base2:.6E} {base2_symbol}"
                  f" ({base__vs_base2_deviations}{base__vs_base2_spread:.6f} ‰)")

            print(f"Источник1: {url1}")
            print(f"Источник2: {url2}")

            print(f"Момент UTC-времени1: {time1_2}")
            print(f"Момент UTC-времени2: {time2_2}")

            print(f"Длительность запроса1: {d_time1}")
            print(f"Длительность запроса2: {d_time2}")
            print(f"Длительность запросов: {d_time}")



            mb.showinfo("Курсы обмена валют", (f"Текущие цены покупки / продажи валюты, включая спред: \n"
                                                f" 1 {base__symbol} ⇄ {data1_base__exchange_rate:.6E} / "
                                                f"{data2_base__exchange_rate:.6E} {base0_symbol} "
                                                f"({base__exchange_rate_deviations}{base__exchange_rate_spread:.6f} ‰)\n"
                                                f""
                                                f" 1 {base0_symbol} ⇄ {data1_base0_exchange_rate:.6E} / "
                                                f"{data2_base0_exchange_rate:.6E} {base0_symbol} "
                                                f"({base0_exchange_rate_deviations}{base0_exchange_rate_spread:.6f} ‰)\n"
                                                f""
                                                f" 1 {base1_symbol} ⇄ {data1_base1_exchange_rate:.6E} / "
                                                f"{data2_base1_exchange_rate:.6E} {base0_symbol} "
                                                f"({base1_exchange_rate_deviations}{base1_exchange_rate_spread:.6f} ‰)\n"
                                                f""
                                                f" 1 {base2_symbol} ⇄ {data1_base2_exchange_rate:.6E} / "
                                                f"{data2_base2_exchange_rate:.6E} {base0_symbol} "
                                                f"({base2_exchange_rate_deviations}{base2_exchange_rate_spread:.6f} ‰)\n"
                                                f"\n"
                                                f"Источник1: {url1}\n"
                                                f"Источник2: {url2}\n"
                                                f"\n"
                                                f"Момент UTC-времени1: {time1_2}\n"
                                                f"Момент UTC-времени2: {time2_2}\n"
                                                f"\n"
                                                f"Длительность запроса1: {d_time1}\n"
                                                f"Длительность запроса2: {d_time2}\n"
                                                f"Длительность запросов: {d_time}"
                                                f""))

        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Задайте все три валюты!")


# Предопределение глобальных переменных


"""Печать словаря с форматированием
ШАГ 1. Создаём словарь Python (пример)
user_data = {
    "name": "Иван Иванов",
    "age": 30,
    "is_active": True,
    "courses": ["Python", "Git"],
    "passport": None
}
print(user_data)
"""
"""
ШАГ 2. Преобразуем словарь в JSON-строку (пример):
json_string = json.dumps(user_data)
print(json_string)
"""
# {
#   "rates": {
#     "btc": {
#       "name": "Bitcoin",
#       "unit": "BTC",
#       "value": 1.0,
#       "type": "crypto"
#     },
#     "eth": {
#       "name": "Ether",
#       "unit": "ETH",
#       "value": 34.292,
#       "type": "crypto"
#     },
# Coingecko-словарь кратких наименований и трёхбуквенных кодов валют
# (с указанием страны-эмитента, соответствующей части света и типа валюты).
# В настоящий момент это 95 валют (14 крипто-, 1 синтетическая и 78 фиатных валют, а также 2 драгметалла).
currencies = {
    "ВНИМАНИЕ! Выберите валюту или введите её код!": "350 шт. (4 металла, 1 синтетик, 150 фиатов и 200 криптовалют)",
    " ": "",
    "ЧАСТЬ1. ДРАГОЦЕННЫЕ МЕТАЛЛЫ": "4 штуки по алфавиту",
    "Золото (тройская унция): XAU": "xau",
    "Серебро (тройская унция): XAG": "xag",
    "Палладий (тройская унция, металл): XPD": "xpd",
    "Платина (тройская унция, металл): XPT": "xpt",
    "  ": "",
    "ЧАСТЬ2. СИНТЕТИЧЕСКИЕ ВАЛЮТЫ": "1 штука",
    "СПЗ МВФ (США, АМЕРИКА, синтетик): XDR": "xdr",
    "   ": "",
    "ЧАСТЬ3. ФИАТНЫЕ ВАЛЮТЫ": "145 штук по алфавиту",
    "Афгани (Афганистан, АЗИЯ): AFN": "afn",
    "Бальбоа (Панама, АМЕРИКА): PAB": "pab",
    "Бат (Таиланд, АЗИЯ): THB": "thb",
    "Боливар (Венесуэла, АМЕРИКА): VES": "ves",
    "Боливиано (Боливия, АМЕРИКА): BOB": "bob",
    "Быр (Эфиопия, АФРИКА): ETB": "etb",
    "Вату (Вануату, ОКЕАНИЯ): VUV": "vuv",
    "Вона (Корея, АЗИЯ): KRW": "krw",
    "Гривна (Украина, ЕВРОПА): UAH": "uah",
    "Гуарани (Парагвай, АМЕРИКА): PYG": "pyg",
    "Гульден (Антильские острова (Нидерланды), АМЕРИКА): ANG": "ang",
    "Гурд (Гаити, АМЕРИКА): HTG": "htg",
    "Даласи (Гамбия, АФРИКА): GMD": "gmd",
    "Денар (Северная Македония, ЕВРОПА): MKD": "mkd",
    "Динар (Алжир, АФРИКА): DZD": "dzd",
    "Динар (Бахрейн, АЗИЯ): BHD": "bhd",
    "Динар (Иордания, АЗИЯ): JOD": "jod",
    "Динар (Ирак, АЗИЯ): IQD": "iqd",
    "Динар (Кувейт, АЗИЯ): KWD": "kwd",
    "Динар (Ливия, АФРИКА): LYD": "lyd",
    "Динар (Сербия, ЕВРОПА): RSD": "rsd",
    "Динар (Тунис, АФРИКА): TND": "tnd",
    "Дирхам (Марокко, АФРИКА): MAD": "mad",
    "Дирхам (ОАЭ, АЗИЯ): AED": "aed",
    "Доллар (Австралия, ОКЕАНИЯ): AUD": "aud",
    "Доллар (Багамы, АМЕРИКА): BSD": "bsd",
    "Доллар (Барбадос, АМЕРИКА): BBD": "bbd",
    "Доллар (Белиз, АМЕРИКА): BZD": "bzd",
    "Доллар (Бермуды (Великобритания), АМЕРИКА): BMD": "bmd",
    "Доллар (Бруней, АЗИЯ): BND": "bnd",
    "Доллар (Гайана, АМЕРИКА): GYD": "gyd",
    "Доллар (Гонконг (Китай), АЗИЯ): HKD": "hkd",
    "Доллар (Каймановы острова (Великобритания), АМЕРИКА): KYD": "kyd",
    "Доллар (Канада, АМЕРИКА): CAD": "cad",
    "Доллар (Либерия, АФРИКА): LRD": "lrd",
    "Доллар (Намибия, АФРИКА): NAD": "nad",
    "Доллар (Новая Зеландия, ОКЕАНИЯ): NZD": "nzd",
    "Доллар (ОВКГ, АМЕРИКА): XCD": "xcd",
    "Доллар (Сингапур, АЗИЯ): SGD": "sgd",
    "Доллар (Соломоновы Острова, ОКЕАНИЯ): SBD": "sbd",
    "Доллар (Суринам, АМЕРИКА): SRD": "srd",
    "Доллар (США, АМЕРИКА): USD": "usd",
    "Доллар (Тайвань, АЗИЯ): TWD": "twd",
    "Доллар (Тринидад и Тобаго, АМЕРИКА): TTD": "ttd",
    "Доллар (Фиджи, ОКЕАНИЯ): FJD": "fjd",
    "Доллар (Ямайка, АМЕРИКА): JMD": "jmd",
    "Донг (Вьетнам, АЗИЯ): VND": "vnd",
    "Драм (Армения, ЕВРАЗИЯ): AMD": "amd",
    "Евро (Евросоюз, ЕВРОПА): EUR": "eur",
    "Злотый (Польша, ЕВРОПА): PLN": "pln",
    "Золотой (Зимбабве, АФРИКА): ZWG": "zwg",
    "Иена (Япония, АЗИЯ): JPY": "jpy",
    "Кванза (Ангола, АФРИКА): AOA": "aoa",
    "Квача (Малави, АФРИКА): MWK": "mwk",
    "Кетсаль (Гватемала, АМЕРИКА): GTQ": "gtq",
    "Кина (Папуа Новая Гвинея, ОКЕАНИЯ): PGK": "pgk",
    "Кип (Лаос, АЗИЯ): LAK": "lak",
    "Колон (Коста-Рика, АМЕРИКА): CRC": "crc",
    "Кордоба (Никарагуа, АМЕРИКА): NIO": "nio",
    "Крона (Дания, ЕВРОПА): DKK": "dkk",
    "Крона (Исландия, ЕВРОПА): ISK": "isk",
    "Крона (Норвегия, ЕВРОПА): NOK": "nok",
    "Крона (Чехия, ЕВРОПА): CZK": "czk",
    "Крона (Швеция, ЕВРОПА): SEK": "sek",
    "Кьят (Мьянма, АЗИЯ): MMK": "mmk",
    "Лари (Грузия, ЕВРАЗИЯ): GEL": "gel",
    "Лей (Молдова, ЕВРОПА): MDL": "mdl",
    "Лей (Румыния, ЕВРОПА): RON": "ron",
    "Лек (Албания, ЕВРОПА): ALL": "all",
    "Лемпира (Гондурас, АМЕРИКА): HNL": "hnl",
    "Леоне (Сьерра-Леоне, АФРИКА): SLL": "sll",
    "Лилангени (Эсватини, АФРИКА): SZL": "szl",
    "Лира (Турция, ЕВРАЗИЯ): TRY": "try",
    "Лоти (Лесото, АФРИКА): LSL": "lsl",
    "Манат (Азербайджан, АЗИЯ): AZN": "azn",
    "Марка (Босния и Герцеговина, ЕВРОПА): BAM": "bam",
    "Найра (Нигерия, АФРИКА): NGN": "ngn",
    "Накфа (Эритрея, АФРИКА): ERN": "ern",
    "Нгултрум (Бутан, АЗИЯ): BTN": "btn",
    "Паанга (Тонга, ОКЕАНИЯ): TOP": "top",
    "Патака (Макао (Китай), АЗИЯ): MOP": "mop",
    "Песо (Аргентина, АМЕРИКА): ARS": "ars",
    "Песо (Доминикана, АМЕРИКА): DOP": "dop",
    "Песо (Колумбия, АМЕРИКА): COP": "cop",
    "Песо (Куба, АМЕРИКА): CUP": "cup",
    "Песо (Мексика, АМЕРИКА): MXN": "mxn",
    "Песо (Уругвай, АМЕРИКА): UYU": "uyu",
    "Песо (Филиппины, АЗИЯ): PHP": "php",
    "Песо (Чили, АМЕРИКА): CLP": "clp",
    "Пула (Ботсвана, АФРИКА): BWP": "bwp",
    "Реал (Бразилия, АМЕРИКА): BRL": "brl",
    "Риал (Иран, АЗИЯ): IRR": "irr",
    "Риал (Йемен, АЗИЯ): YER": "yer",
    "Риал (Катар, АЗИЯ): QAR": "qar",
    "Риал (Оман, АЗИЯ): OMR": "omr",
    "Риель (Камбоджа, АЗИЯ): KHR": "khr",
    "Ринггит (Малайзия, АЗИЯ): MYR": "myr",
    "Риял (Саудовская Аравия, АЗИЯ): SAR": "sar",
    "Рубль (Беларусь, ЕВРОПА): BYN": "byn",
    "Рубль (Россия, ЕВРАЗИЯ): RUB": "rub",
    "Рупия (Индия, АЗИЯ): INR": "inr",
    "Рупия (Индонезия, АЗИЯ): IDR": "idr",
    "Рупия (Маврикий, АФРИКА): MUR": "mur",
    "Рупия (Непал, АЗИЯ): NPR": "npr",
    "Рупия (Пакистан, АЗИЯ): PKR": "pkr",
    "Рупия (Сейшелы, АФРИКА): SCR": "scr",
    "Рупия (Шри-Ланка, АЗИЯ): LKR": "lkr",
    "Руфия (Мальдивы, АЗИЯ): MVR": "mvr",
    "Рэнд (ЮАР, АФРИКА): ZAR": "zar",
    "Соль (Перу, АМЕРИКА): PEN": "pen",
    "Сом (Кыргызстан, АЗИЯ): KGS": "kgs",
    "Сомони (Таджикистан, АЗИЯ): TJS": "tjs",
    "Сум (Узбекистан, АЗИЯ): UZS": "uzs",
    "Така (Бангладеш, АЗИЯ): BDT": "bdt",
    "Тала (Самоа, ОКЕАНИЯ): WST": "wst",
    "Тенге (Казахстан, ЕВРАЗИЯ): KZT": "kzt",
    "Тугрик (Монголия, АЗИЯ): MNT": "mnt",
    "Флорин (Аруба (Нидерланды), АМЕРИКА): AWG": "awg",
    "Форинт (Венгрия, ЕВРОПА): HUF": "huf",
    "Франк (Бурунди, АФРИКА): BIF": "bif",
    "Франк (Гвинея, АФРИКА): GNF": "gnf",
    "Франк (ГЗА, АФРИКА): XOF": "xof",
    "Франк (ГЦА, АФРИКА): XAF": "xaf",
    "Франк (Джибути, АФРИКА): DJF": "djf",
    "Франк (Заморские территории (Франция), ОКЕАНИЯ): XPF": "xpf",
    "Франк (Коморы, АФРИКА): KMF": "kmf",
    "Франк (Конго, АФРИКА): CDF": "cdf",
    "Франк (Руанда, АФРИКА): RWF": "rwf",
    "Франк (Швейцария, ЕВРОПА): CHF": "chf",
    "Фунт (Великобритания, ЕВРОПА): GBP": "gbp",
    "Фунт (Египет, АФРИКА): EGP": "egp",
    "Фунт (Ливан, АЗИЯ): LBP": "lbp",
    "Фунт (Святой Елены (Великобритания), АФРИКА): SHP": "shp",
    "Фунт (Сирия, АЗИЯ): SYP": "syp",
    "Фунт (Судан, АФРИКА): SDG": "sdg",
    "Фунт (Фолклендские острова (Великобритания), АМЕРИКА): FKP": "fkp",
    "Фунт (Южный Судан, АФРИКА): SSP": "ssp",
    "Шекель (Израиль, АЗИЯ): ILS": "ils",
    "Шиллинг (Кения, АФРИКА): KES": "kes",
    "Шиллинг (Сомалиленд, АФРИКА): SOS": "sos",
    "Шиллинг (Танзания, АФРИКА): TZS": "tzs",
    "Шиллинг (Уганда, АФРИКА): UGX": "ugx",
    "Эскудо (Кабо-Верде, АФРИКА): CVE": "cve",
    "Юань (Китай, АЗИЯ): CNY": "cny",
    "    ": "",
    "ЧАСТЬ4. КРИПТОВАЛЮТЫ": "Топ-200 из 225000+ шт.",
    "Биткоин (крипта): BTC": "btc",
    "Эфириум (крипта): ETH": "eth",
    "Тетер USDt (крипта): USDT": "usdt",
    "BNB (крипта): BNB": "bnb",
    "XRP (крипта): XRP": "xrp",
    "USDC (крипта): USDC": "usdc",
    "Солана (крипта): SOL": "sol",
    "ТРОН (крипта): TRX": "trx",
    "Zcash (крипта): ZEC": "zec",
    "Гиперликвидность (крипта): HYPE": "hype",
    "Догекоин (крипта): DOGE": "doge",
    "Монеро (крипта): XMR": "xmr",
    "Чейнлинк (крипта): LINK": "link",
    "UNUS SED LEO (крипта): LEO": "leo",
    "Кардано (крипта): ADA": "ada",
    "Стеллар (крипта): XLM": "xlm",
    "Биткоин Кэш (крипта): BCH": "bch",
    "NEAR Протокол (крипта): NEAR": "near",
    "Унисвап (крипта): UNI": "uni",
    "Эфина USDe (крипта): USDe": "usde",
    "Дай (крипта): DAI": "dai",
    "Лайткоин (крипта): LTC": "ltc",
    "Лавина (крипта): AVAX": "avax",
    "Кантон (крипта): CC": "cc",
    "Суи (крипта): SUI": "sui",
    "Мировая финансовая свобода USD (крипта): USD1": "usd1",
    "Грам (ранее Тонкоин) (крипта): GRAM": "gram",
    "Хедера (крипта): HBAR": "hbar",
    "Тетер Голд (крипта): XAUt": "xaut",
    "Сиба Ину (крипта): SHIB": "shib",
    "Глобал Доллар (крипта): USDG": "usdg",
    "Биттенсор (крипта): TAO": "tao",
    "PayPal USD (крипта): PYUSD": "pyusd",
    "Кронос (крипта): CRO": "cro",
    "Риппл USD (крипта): RLUSD": "rlusd",
    "Квант (крипта): QNT": "qnt",
    "Эфина (крипта): ENA": "ena",
    "ОКБ (крипта): OKB": "okb",
    "Пепе (крипта): PEPE": "pepe",
    "Ааве (крипта): AAVE": "aave",
    "Ондо (крипта): ONDO": "ondo",
    "Астер (крипта): ASTER": "aster",
    "Памп.фун (крипта): PUMP": "pump",
    "МемеКоре (крипта): M": "m",
    "PAX Голд (крипта): PAXG": "paxg",
    "Полкадот (крипта): DOT": "dot",
    "Юнайтед Стейблс (крипта): U": "u",
    "Мантл (крипта): MNT": "mnt",
    "Скай (крипта): SKY": "sky",
    "Мировая финансовая свобода (крипта): WLFI": "wlfi",
    "USDD (крипта): USDD": "usdd",
    "Интернет Компьютер (крипта): ICP": "icp",
    "Миркоин (крипта): WLD": "wld",
    "Битгет Токен (крипта): BGB": "bgb",
    "Morpho (крипта): MORPHO": "morpho",
    "Ethereum Classic (крипта): ETC": "etc",
    "Arbitrum (крипта): ARB": "arb",
    "JUST (крипта): JST": "jst",
    "Venice Token (крипта): VVV": "vvv",
    "Аэро (крипта): AERO": "aero",
    "GateToken (крипта): GT": "gt",
    "КуКойн Токен (крипта): KCS": "kcs",
    "Полигон (ранее MATIC) (крипта): POL": "pol",
    "Алгоранд (крипта): ALGO": "algo",
    "Каспа (крипта): KAS": "kas",
    "Зажигалка (крипта): LIT": "lit",
    "Пи (крипта): PI": "pi",
    "Юпитер (крипта): JUP": "jup",
    "Рендер (крипта): RENDER": "render",
    "Космос (крипта): ATOM": "atom",
    "Инъекционный (крипта): INJ": "inj",
    "LayerZero (крипта): ZRO": "zro",
    "Файлкойн (крипта): FIL": "fil",
    "Midnight (крипта): NIGHT": "night",
    "XDC Network (крипта): XDC": "xdc",
    "PancakeSwap (крипта): CAKE": "cake",
    "Stacks (крипта): STX": "stx",
    "Dash (крипта): DASH": "dash",
    "ether.fi (крипта): ETHFI": "ethfi",
    "Aptos (крипта): APT": "apt",
    "Flare (крипта): FLR": "flr",
    "Pyth Network (крипта): PYTH": "pyth",
    "币安人生 (крипта): 币安人生": "币安人生",
    "Stable (крипта): STABLE": "stable",
    "VeChain (крипта): VET": "vet",
    "Nexo (крипта): NEXO": "nexo",
    "TrueUSD (крипта): TUSD": "tusd",
    "Raydium (крипта): RAY": "ray",
    "Pudgy Penguins (крипта): PENGU": "pengu",
    "Celestia (крипта): TIA": "tia",
    "EURC (крипта): EURC": "eurc",
    "Curve DAO Token (крипта): CRV": "crv",
    "Kite (крипта): KITE": "kite",
    "Artificial Superintelligence Alliance (крипта): FET": "fet",
    "Virtuals Protocol (крипта): VIRTUAL": "virtual",
    "Sei (крипта): SEI": "sei",
    "SPX6900 (крипта): SPX": "spx",
    "OFFICIAL TRUMP (крипта): TRUMP": "trump",
    "Pieverse (крипта): PIEVERSE": "pieverse",
    "BitTorrent [New] (крипта): BTT": "btt",
    "Bitcoin SV (крипта): BSV": "bsv",
    "Starknet (крипта): STRK": "strk",
    "Falcon Finance (крипта): FF": "ff",
    "Pendle (крипта): PENDLE": "pendle",
    "Plasma (крипта): XPL": "xpl",
    "Sun [New] (крипта): SUN": "sun",
    "Gnosis (крипта): GNO": "gno",
    "First Digital USD (крипта): FDUSD": "fdusd",
    "Lido DAO (крипта): LDO": "ldo",
    "Tezos (крипта): XTZ": "xtz",
    "Bonk (крипта): BONK": "bonk",
    "Optimism (крипта): OP": "op",
    "Conflux (крипта): CFX": "cfx",
    "Immutable (крипта): IMX": "imx",
    "Decred (крипта): DCR": "dcr",
    "Terra Classic (крипта): LUNC": "lunc",
    "The Graph (крипта): GRT": "grt",
    "AINFT (крипта): NFT": "nft",
    "Beam (крипта): BEAM": "beam",
    "FLOKI (крипта): FLOKI": "floki",
    "Kaia (крипта): KAIA": "kaia",
    "Monad (крипта): MON": "mon",
    "Kamino (крипта): KMNO": "kmno",
    "Arweave (крипта): AR": "ar",
    "Ethereum Name Service (крипта): ENS": "ens",
    "THORChain (крипта): RUNE": "rune",
    "Basic Attention Token (крипта): BAT": "bat",
    "Compound (крипта): COMP": "comp",
    "Zebec Network (крипта): ZBCN": "zbcn",
    "Jito (крипта): JTO": "jto",
    "Convex Finance (крипта): CVX": "cvx",
    "JasmyCoin (крипта): JASMY": "jasmy",
    "Fluid (крипта): FLUID": "fluid",
    "Maple Finance (крипта): SYRUP": "syrup",
    "IOTA (крипта): IOTA": "iota",
    "Akash Network (крипта): AKT": "akt",
    "EigenCloud (крипта): EIGEN": "eigen",
    "Zama (крипта): ZAMA": "zama",
    "dogwifhat (крипта): WIF": "wif",
    "Trust Wallet Token (крипта): TWT": "twt",
    "OriginTrail (крипта): TRAC": "trac",
    "Meteora (крипта): MET": "met",
    "SOON (крипта): SOON": "soon",
    "Theta Network (крипта): THETA": "theta",
    "Axie Infinity (крипта): AXS": "axs",
    "GoМining (крипта): GOMINING": "gomining",
    "Pons (крипта): PONS": "pons",
    "Decentraland (крипта): MANA": "mana",
    "MX Token (крипта): MX": "mx",
    "Grass (крипта): GRASS": "grass",
    "Useless Coin (крипта): USELESS": "useless",
    "Onyxcoin (крипта): XCN": "xcn",
    "Vaulta (крипта): A": "a",
    "Neo (крипта): NEO": "neo",
    "The Песочница (крипта): SAND": "sand",
    "Кэп (крипта): CAP": "cap",
    "Видение (крипта): VSN": "vsn",
    "Сентиент (крипта): SENT": "sent",
    "БУИЛДон (крипта): B": "b",
    "Телкоин (крипта): TEL": "tel",
    "AWE (крипта): AWE": "awe",
    "Фарткоин (крипта): FARTCOIN": "fartcoin",
    "eCash (крипта): XEC": "xec",
    "Чилиз (крипта): CHZ": "chz",
    "Сеть AIOZ (крипта): AIOZ": "aioz",
    "1inch (крипта): 1INCH": "1inch",
    "edgeX (крипта): EDGE": "edge",
    "DeXe (крипта): DEXE": "dexe",
    "Соник (крипта): S": "s",
    "СуперВерсия (крипта): SUPER": "super",
    "ApeCoin (крипта): APE": "ape",
    "ZKsync (крипта): ZK": "zk",
    "GEODNET (крипта): GEOD": "geod",
    "Голем (крипта): GLM": "glm",
    "Кэш Кэт (крипта): CASHCAT": "cashcat",
    "SafePal (крипта): SFP": "sfp",
    "Этир (крипта): Ист. макс.": "ист. макс.",
    "Хьюманити (крипта): H": "h",
    "МультиверсX (крипта): EGLD": "egld",
    "Терминал Genius (крипта): GENIUS": "genius",
    "Горизонт (крипта): ZEN": "zen",
    "Плюм (крипта): PLUME": "plume",
    "Пром (крипта): PROM": "prom",
    "GMX (крипта): GMX": "gmx",
    "Протокол DeepBook (крипта): DEEP": "deep",
    "0G (крипта): 0G": "0g",
    "Зарезервированные права (крипта): RSR": "rsr",
    "Орка (крипта): ORCA": "orca",
    "dYdX (крипта): DYDX": "dydx",
    "Собака (Биткоин) (крипта): DOG": "dog",
    "peaq (крипта): PEAQ": "peaq",
    "Гала (крипта): GALA": "gala",
    "USD.AI (крипта): CHIP": "chip",
    "Холо (крипта): HOT": "hot",
    "Тэггер (крипта): TAG": "tag",
    "Протокол 0x (крипта): ZRX": "zrx",
    "RedStone (крипта): RED": "red",
    "DoubleZero (крипта): 2Z": "2z",
    "Qtum (крипта): QTUM": "qtum",
    "Четыре (крипта): FORM": "form"
}
# print('Печать Coingecko-словаря валют без форматирования - одной строкой:')
# print(currencies)

"""
ШАГ 2. Преобразуем словарь в JSON-строку (пример):
json_string = json.dumps(user_data)
print(json_string)
"""
# json_currencies = json.dumps(currencies, indent=2, ensure_ascii=False, encoding="utf-8")
# json_currencies = json.dumps(currencies, indent=2)
# print(json_currencies)  # Странно, получилось частично. Печать словаря стала построчной,
# но вместо наименованя валюты выводится последовательность цифровых кодов
# кирилических символов (коды 0400—04FF через обратный слэш).

"""
Быстрый ответ Алисы AI
Как настроить вывод:
- ensure_ascii=False. По умолчанию этот параметр включён (True), 
  и тогда все не-ASCII символы (в том числе кириллица) экранируются — 
  заменяются на последовательности вроде "_u043a_u043e_u043e_u0444_u0435". 
  Если поставить False, символы останутся читаемыми.
"""
json_currencies = json.dumps(currencies,
                             indent=2,
                             ensure_ascii=False,
                             # encoding="utf-8"
                             )
# print(f"Печать Coingecko-словаря валют с форматированием - построчно: \n"
#       f"с указанием страны-эмитента и соответствующей части света:")
# print(json_currencies)  # Ура! Заработало!

# Создание графического интерфейса
window = Tk()
window.title("Курсы обмена валют")
window.geometry("525x120")

f0 = Frame(window)
f0.pack(pady=(7,0))
f1 = Frame(window)
f1.pack(pady=(5,0))
f2 = Frame(window)
f2.pack(pady=(5,0))
f3 = Frame(window)
f3.pack(pady=(7,0))

Label(f0, text="Платёжная валюта:", justify='left', width=17).pack(side=LEFT)
base0_currency_symbol = ttk.Label(f0, justify='center', width=5)
base0_currency_symbol.pack(side=LEFT)
base0_combobox = ttk.Combobox(f0, values=list(currencies.keys()), width=55, justify='left', state='normal')
base0_combobox.set("Рубль (Россия, ЕВРАЗИЯ): RUB")  # Устанавливаем значение по умолчанию
base0_combobox.pack(side=LEFT)
base0_combobox.bind("<<ComboboxSelected>>", update_base0_currency_symbol)
# base0_combobox.bind('<KeyPress>', update_base0_currency_symbol)  # Привязываем событие нажатия на любую клавишу

Label(f1, text="Обменная валюта1:", justify='left', width=17).pack(side=LEFT)
base1_currency_symbol = ttk.Label(f1, justify='center', width=5)
base1_currency_symbol.pack(side=LEFT)
base1_combobox = ttk.Combobox(f1, values=list(currencies.keys()), width=55, justify='left', state='normal')
base1_combobox.set("syp")  # Устанавливаем значение по умолчанию
base1_combobox.pack(side=LEFT)
base1_combobox.bind("<<ComboboxSelected>>", update_base1_currency_symbol)
# base1_combobox.bind('<KeyPress>', update_base1_currency_symbol)  # Привязываем событие нажатия на любую клавишу

Label(f2, text="Обменная валюта2:", justify='left', width=17).pack(side=LEFT)
base2_currency_symbol = ttk.Label(f2, justify='center', width=5)
base2_currency_symbol.pack(side=LEFT)
base2_combobox = ttk.Combobox(f2, values=list(currencies.keys()), width=55, justify='left', state='normal')
base2_combobox.set("cve")  # Устанавливаем значение по умолчанию
base2_combobox.pack(side=LEFT)
base2_combobox.bind("<<ComboboxSelected>>", update_base2_currency_symbol)
# base2_combobox.bind('<KeyPress>', update_base2_currency_symbol)  # Привязываем событие нажатия на любую клавишу

Button(f3, text=f"Запросите цену покупки и продажи валют на API-сайте!",
       justify='center', command=exchange_rates).pack(side=RIGHT)

window.mainloop()