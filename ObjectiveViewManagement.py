import tkinter as tk
from tkinter import ttk

class ObjectiveFrame(tk.Frame):
    def __init__(self, containter,objective):
        super().__init__(containter)
        label = ttk.Label(self, text='Objective: [' + objective + ']')
        label.grid(column=0, row=0, sticky=tk.NW, padx=1, pady=1)
        self.config(bg='green')