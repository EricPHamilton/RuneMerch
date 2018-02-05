import json

unfiltered = json.load(open('../data/items_unfiltered.json'))
filtered_dict = {}
name_to_id = {}

for key in unfiltered:
    value = unfiltered[key]
    if value['tradeable'] == True:
        filtered_dict[key] = value

        name_to_id[value['name']] = key

with open('../data/id_to_name.json', 'w') as outfile:
    json.dump(filtered_dict, outfile)

with open('../data/name_to_id.json', 'w') as outfile:
    json.dump(name_to_id, outfile)