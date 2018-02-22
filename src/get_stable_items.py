import json
import runescape_api_calls
import data_calls

def count_spikes(prices, margin):
    daily = prices[1]
    aver = prices[0]
    ctr = 0

    for day in daily:
        day_price = int(daily[day])
        aver_price = int(aver[day])

        diff = abs((day_price - aver_price) / (aver_price))
        if diff > margin:
            ctr += 1

    return ctr

items = json.load(open('../data/id_to_name.json'))

for id in items:
    name = items[id]

    hists = data_calls.get_price_from_json(id)
    spikes = count_spikes(hists, .05)
    print(id, spikes)




