import tkinter as tk
from tkinter import ttk
from random import randrange
from Conversation import Dialog

class RandFeatureSelector():
    img_list = ['house1.png','mlake.png','monst1.png']
    #def __init__(self):
    #do nothing
    def getRandFeature(self):
        return self.img_list[randrange(len(self.img_list))]

class MapCellFrame(tk.Frame):
    row_number =0
    col_number =0
    feature_file = 'dummy.png'
    download_icon = None
    gameControl = None
    def __init__(self, containter,row,col, control):
        super().__init__(containter)
        self.gameControl = control
        feat = RandFeatureSelector()
        self.row_number = row
        self.col_number = col
        cont_text = "{}x{}".format(self.row_number,self.col_number)
        label = ttk.Label(self, text=cont_text)
        label.grid(column=0, row=0, sticky='nsew', padx=2, pady=2)
        self.feature_file = './assets/{}'.format(feat.getRandFeature())
        self.download_icon = tk.PhotoImage(file=self.feature_file)
        button = ttk.Button(self, image=self.download_icon, command=self.btn_clicked)
        button.grid(column=0, row=1, sticky='nsew', padx=2, pady=2)
        self.config(bg='green')

    def receiveResponse(self, resp):
        #todo: pass response to cell feature for reaction and passing to game controller
        print('Response Received: {}'.format(len(resp.getResponseData())))

    def btn_clicked(self):
        print('Clicked On: {}'.format(self.feature_file))
        #todo: tell asociated feature of an intial interaction.
        #for now, create mock Dialog and pass to game controller
        d = Dialog('Please Feed Me!{}-{}'.format(self.row_number,self.col_number),[(1,'No'),(2,'Sure'),(3,'Feed Yourself!')])
        self.gameControl.displayDialog(d,self)
