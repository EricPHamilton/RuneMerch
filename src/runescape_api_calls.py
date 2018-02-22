import requests
import json
import time


def get_price_history_from_id(id):
    f = requests.get('http://services.runescape.com/m=itemdb_rs/viewitem?obj=' + id)

    text = f.text
    avg_prices = []
    daily_prices = []

    for line in text.split("\n"):
        if 'blocked' in line:
            #Too many recent requests. Need to sleep and redo this request.
            print("Too many requests. Redoing id:", id)
            time.sleep(60)
            return get_price_history_from_id(id)

        if 'average180.push' in line:
            arr = line.split(", ")
            avg_prices.append(int(arr[1]))
            daily_prices.append(int(arr[2].split(']')[0]))

    return (avg_prices, daily_prices)