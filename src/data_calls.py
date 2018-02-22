import json

def get_price_from_json(id):
    data = json.load(open('../data/prices_2018-02-21-15.json'))
    return (data[str(id)]['daily_prices'], data[str(id)]['avg_prices'])