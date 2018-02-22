import json
import runescape_api_calls
import datetime

items = json.load(open('../data/id_to_name.json'))
fname = datetime.datetime.now().strftime('../data/prices_%Y-%m-%d-%H.json')
data = {}

for id in items:
    print("Getting prices for: " + id)
    name = items[id]

    hists = runescape_api_calls.get_price_history_from_id(id)
    avg_prices = hists[0]
    daily_prices = hists[1]

    data[id] = {"avg_prices": avg_prices, "daily_prices": daily_prices,}

    if len(data) % 25 == 0:
        with open(fname, 'w') as outfile:
            json.dump(data, outfile)
            print("Written for", len(data))