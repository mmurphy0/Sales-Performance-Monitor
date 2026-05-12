import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

import pandas as pd

import matplotlib.pyplot as plt

from time import strftime

def add_new_sale():
    add_sale_win = Toplevel()
    add_sale_win.geometry('+0+0')
    add_sale_win.resizable(False,False)
    add_sale_win.title('Sales Performance Monitor - Add new sale')

def view_sales():
    df = pd.read_csv('sales_date.csv')

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
    width=28
    # command=add_new_sale
)
add_sale_button.pack()

view_sales_button = tk.Button(
    root,
    text='View Sales',
    font=('Arial'),
    width=28
    # command=view_sales_performance
)
view_sales_button.pack()

root.mainloop()