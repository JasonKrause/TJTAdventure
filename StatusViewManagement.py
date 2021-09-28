import tkinter as tk
from tkinter import ttk

class StatusFrame(tk.Frame):
    def __init__(self, containter,state):
        super().__init__(containter,width=300)
        label = ttk.Label(self, text='state: [' + state + ']')
        label.grid(column=0, row=0, sticky=tk.NW, padx=1, pady=1)
        self.config(bg='green')