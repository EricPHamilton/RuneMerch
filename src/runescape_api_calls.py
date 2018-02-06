import requests
import json

def get_price_history_from_id(id):
    r = requests.get('http://services.runescape.com/m=itemdb_rs/api/graph/' + id + '.json')
    return json.loads(r.content)