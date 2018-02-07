from runescape_api_calls import *
import matplotlib.pyplot as plot
from tkinter import *
import json
import datetime
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def get_names():
    names = []
    list = json.load(open('../data/name_to_id.json'))
    for key in list:
        value = list[key]
        names.append(key + ":" + value)
    return names

def display_graph(id):
    print(id)
    json = get_price_history_from_id(id)
    plot_data = extract_plot_data(json)

def extract_plot_data(json):
    plot.close()
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

    return x_axis, daily_axis, average_axis

class MyWindow(Frame):
    def populate_options(self):
        names = get_names()
        for key in names:
            self.listbox.insert(END, key)
        self.listbox.pack()
        all_items = self.listbox.get(0, END)
        return all_items

    def __init__(self, parent):
        def update_listbox(*args):
            search_term = search_var.get()
            self.listbox.delete(0, END)
            for item in all_items:
                if search_term.lower() in item.lower():
                    self.listbox.insert(END, item)

        def update_graph(evt):
            '''
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)

            cur_id = value.split(':')[1]
            print(cur_id)

            json = get_price_history_from_id(cur_id)

            plot_data = extract_plot_data(json)
            print(plot_data[0])
            print(plot_data[1])
            print(plot_data[2])

            self.fig.canvas.draw()'''


        Frame.__init__(self, parent)
        search_var = StringVar()
        search_var.trace('w', update_listbox)
        searchbox = Entry(master, textvariable=search_var)
        searchbox.pack(fill=X, expand=False)

        self.listbox = Listbox(master)
        all_items = MyWindow.populate_options(self)

        f = Figure(figsize=(5, 5))
        a = f.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack()

        self.listbox.bind('<<ListboxSelect>>', update_graph)

master = Tk()
MyWindow(master).pack()
master.mainloop()