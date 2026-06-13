import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

import pandas as pd

import matplotlib.pyplot as plt

from time import strftime

import csv

def add_new_sale():
    def save_sale():
        current_time = str(strftime('%H:%M:%S %D'))
        sales_value = str(value_entry.get())
        salesperson_choice = str(chosen_radiobutton.get())
        with open('sales_data.csv','a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, sales_value, salesperson_choice])
            messagebox.showinfo('Confirmation','Sale saved successfully')
            add_sale_win.destroy()

    add_sale_win = Toplevel()
    add_sale_win.geometry('+0+0')
    add_sale_win.resizable(False,False)
    add_sale_win.title('Sales Performance Monitor - Add new sale')

    add_sale_label = tk.Label(
        add_sale_win,
        text='Add New Sale',
        font=('Arial',20,'bold')
    )
    add_sale_label.grid(
        row=1,
        column=1,
        columnspan=4
    )

    radiobutton_title = tk.Label(
        add_sale_win,
        text='Salespeople:',
        font=('Arial')
    )
    radiobutton_title.grid(
        row=2,
        column=1,
        columnspan=2
    )

    chosen_radiobutton = tk.StringVar(value='Salesperson 1')

    salesperson1_radiobutton = tk.Radiobutton(
        add_sale_win,
        text='Salesperson 1',
        font=('Arial'),
        variable=chosen_radiobutton,
        value='Salesperson 1'
    )
    salesperson1_radiobutton.grid(
        row=3,
        column=1,
        columnspan=2
    )

    salesperson2_radiobutton = tk.Radiobutton(
        add_sale_win,
        text='Salesperson 2',
        font=('Arial'),
        variable=chosen_radiobutton,
        value='Salesperson 2'
    )
    salesperson2_radiobutton.grid(
        row=4,
        column=1,
        columnspan=2
    )

    salesperson3_radiobutton = tk.Radiobutton(
        add_sale_win,
        text='Salesperson 3',
        font=('Arial'),
        variable=chosen_radiobutton,
        value='Salesperson 3'
    )
    salesperson3_radiobutton.grid(
        row=3,
        column=3,
        columnspan=2
    )

    salesperson4_radiobutton = tk.Radiobutton(
        add_sale_win,
        text='Salesperson 4',
        font=('Arial'),
        variable=chosen_radiobutton,
        value='Salesperson 4'
    )
    salesperson4_radiobutton.grid(
        row=4,
        column=3,
        columnspan=2
    )

    value_text_label = tk.Label(
        add_sale_win,
        text='Sales Value: £',
        font=('Arial')
    )
    value_text_label.grid(
        row=5,
        column=1,
        columnspan=2
    )

    value_entry = tk.Entry(
        add_sale_win,
        width=10
    )
    value_entry.grid(
        row=5,
        column=3
    )

    save_button = tk.Button(
        add_sale_win,
        text='Add Sale',
        font=('Arial'),
        width=20,
        command=save_sale
    )
    save_button.grid(
        row=6,
        column=1,
        columnspan=4
    )

def view_sales_performance():
    df = pd.read_csv('sales_data.csv')

    totals = df.groupby('Salesperson')['Value'].sum()

    plt.bar(totals.index, totals.values)
    plt.xlabel('Salesperson')
    plt.ylabel('Sales Value £')
    plt.title('Sales performance by Salesperson')
    plt.show()
    

root = tk.Tk()
root.geometry('+0+0')
root.resizable(False,False)
root.title('Sales Performance Monitor')

root_label = tk.Label(
    root,
    text='Sales Performance Monitor',
    font=('Arial',20,'bold')
)
root_label.pack()

add_sale_button = tk.Button(
    root,
    text='Add Sale',
    font=('Arial'),
    width=28,
    command=add_new_sale
)
add_sale_button.pack()

view_sales_button = tk.Button(
    root,
    text='View Sales',
    font=('Arial'),
    width=28,
    command=view_sales_performance
)
view_sales_button.pack()

root.mainloop()