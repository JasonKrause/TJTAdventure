import tkinter as tk
from tkinter import ttk

class InventoryFrame(tk.Frame):
    def __init__(self, containter,title):
        super().__init__(containter, width=100, height=100)
        label = ttk.Label(self, text='inventory: [' + title + ']')
        label.grid(column=0, row=0, sticky=tk.NW, padx=1, pady=1)
        self.config(bg='green')


#class InventoryType():

class InventoryItem():
    def __init__(self,t):
        self.type = t

class InvSlotFrame(tk.Frame):
    row_number =0
    col_number =0
    gameControl = None
    item = None
    def __init__(self, containter,row,col, control):
        super().__init__(containter)
        self.gameControl = control
        self.row_number = row
        self.col_number = col

    def setSlotItem(self, invItem):
        self.item = invItem