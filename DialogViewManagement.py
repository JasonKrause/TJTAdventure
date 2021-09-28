import tkinter as tk
from tkinter import ttk
from Conversation import Response

class DialogFrame(tk.Frame):
    label = None
    mapCellContext = None
    dialog = None
    def __init__(self, containter,title):
        super().__init__(containter)
        self.label = ttk.Label(self, text='dialog: [' + title + ']')
        self.label.grid(column=0, row=0, sticky=tk.NW, padx=1, pady=1)
        self.text = tk.StringVar()
        self.textbox = ttk.Entry(self, textvariable=self.text)
        self.textbox.grid(column=1, row=0, sticky='ns', padx=1, pady=1)
        self.btn = ttk.Button(
            self,
            text="Submit",
            command=self.showSelected
        )
        self.btn.grid(column=2, row=0, sticky='ns', padx=1, pady=1)
        self.config(bg='green')

    def displayDialog(self,d,mapCell):
        self.mapCellContext = mapCell
        self.dialog = d
        dispText = 'Ask: {}\n'.format(d.getAskText())
        for key,value in d.getResponseOptions():
            dispText += 'Code: {}; Value: {}\n'.format(key,value)
        self.label['text'] = dispText

    def showSelected(self):
        print('Selected Text:{}'.format(self.text.get()))
        resp = Response()
        resp.updateResponseData('dialog',self.dialog)
        resp.updateResponseData('optionSelected',self.text.get())
        self.mapCellContext.receiveResponse(resp)