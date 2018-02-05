from runescape_api_calls import *
import matplotlib.pyplot as plot
from tkinter import *
import json
import datetime

master = Tk()

def get_names():
    names = []
    list = json.load(open('../data/name_to_id.json'))
    for key in list:
        value = list[key]
        names.append(key + ":" + value)

    return names

def update_listbox(*args):
    search_term = search_var.get()
    listbox.delete(0, END)
    for item in all_items:
        if search_term.lower() in item.lower():
            listbox.insert(END, item)

search_var = StringVar()
search_var.trace('w', update_listbox)
searchbox = Entry(master, textvariable=search_var)
searchbox.pack(fill=X, expand=False)

listbox = Listbox(master)
names = get_names()
for key in names:
    listbox.insert(END, key)
listbox.pack()
all_items = listbox.get(0, END)

def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)

    cur_id = value.split(':')[1]
    display_graph(cur_id)

def display_graph(id):
    print(id)
    json = get_price_history_from_id(id)
    plot_data = extract_plot_data(json)

def extract_plot_data(json):
    daily = json['daily']
    average = json['average']

    x_axis = []
    daily_axis = []
    average_axis = []

    for key in daily:
        daily_value = daily[key]
        average_value = average[key]
        x_axis.append(datetime.datetime.fromtimestamp(int(key)/1000.0))
        daily_axis.append(daily_value)
        average_axis.append(average_value)

    plot.plot(x_axis, daily_axis)
    plot.plot(x_axis, average_axis)
    plot.show()

listbox.bind('<<ListboxSelect>>', onselect)

master.mainloop()