import tkinter as tk
from tkinter import ttk
from Control import PlayerStatsModifier
from random import randrange

class RandInvSelector():
    img_list = ['sword1.png','potion1.png','shirt1.png','misc.png']
    #def __init__(self):
    #do nothing
    def getRandInv(self):
        return self.img_list[randrange(len(self.img_list))]

class InventoryType():
    def __init__(self, typeStr="misc"):
        self.type = typeStr

    def __str__(self):
        return self.type

class InventoryItem():
    def __init__(self, name="noname", iType=InventoryType("misc"), imageFile="misc.png", context=""):
        self.imageFilename = imageFile
        self.invType = iType
        self.statsMod = PlayerStatsModifier()
        self.name = name
        self.context = context

    def __str__(self):
        return "Context: {} Name: {} Type: {} StatsMod: {}".format(self.context, self.name, self.invType, self.statsMod)

class InventoryFrame(tk.Frame):

    def __init__(self, containter, title, control):
        super().__init__(containter)
        label = ttk.Label(self, text='inventory1: [' + title + ']')
        label.grid(column=0, row=0, sticky=tk.NW, padx=1, pady=1)
        self.config(bg='green')
        inv = InvSlotFrame(self, 2, 3, control, context="INV1")
        inv.grid(column=0, row=1, sticky='nsew', padx=1, pady=1)
        label = ttk.Label(self, text='inventory2: [' + title + ']')
        label.grid(column=0, row=2, sticky=tk.NW, padx=1, pady=1)
        self.config(bg='green')
        inv = InvSlotFrame(self, 2, 4, control, context="INV2")
        inv.grid(column=0, row=3, sticky='nsew', padx=1, pady=1)

class InventoryCellFrame(tk.Frame):
    row_number =0
    col_number =0
    feature_file = 'dummy.png'
    download_icon = None
    gameControl = None

    def __init__(self, containter,row,col, control, context):
        super().__init__(containter)
        self.gameControl = control
        self.context = context
        #temp test item for now. need blank item type as default
        rnd = RandInvSelector()


        self.invItem = InventoryItem(name="R{}xC{}".format(row, col), imageFile=rnd.getRandInv(), context=self.context)
        self.invItem.statsMod.str = randrange(5)
        self.invItem.statsMod.dex = randrange(5)
        self.invItem.statsMod.itl = randrange(5)
        self.invItem.statsMod.cha = randrange(5)
        self.invItem.statsMod.con = randrange(5)
        self.invItem.statsMod.wis = randrange(5)
        image = self.invItem.imageFilename
        self.row_number = row
        self.col_number = col
        cont_text = "{}x{}".format(self.row_number,self.col_number)
        label = ttk.Label(self, text=cont_text)
        label.grid(column=0, row=0, sticky='nsew', padx=2, pady=2)
        self.feature_file = './assets/{}'.format(image)
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
        #d = Dialog('Please Feed Me!{}-{}'.format(self.row_number,self.col_number),[(1,'No'),(2,'Sure'),(3,'Feed Yourself!')])
        self.gameControl.selectInventoryItem(self.invItem)



class InvSlotFrame(tk.Frame):
    row_number = 0
    col_number = 0
    gameControl = None
    item = None
    context = ""

    def __init__(self, containter, row, col, control, context):
        super().__init__(containter)
        self.gameControl = control
        self.row_number = row
        self.col_number = col
        self.context = context
        for r in range(row):
            self.grid_rowconfigure(r, minsize=50,weight=1)
            for c in range(col):
                self.grid_columnconfigure(c, minsize=45, weight=1)
                cellFrame = InventoryCellFrame(self, r, c, self.gameControl, self.context)
                cellFrame['bg'] = 'green'
                cellFrame.grid(column=c, row=r, sticky='nsew')

    #def setSlotItem(self, invItem):
    #    self.item = invItem