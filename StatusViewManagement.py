import tkinter as tk
from tkinter import ttk
from Control import PlayerStats

class StatusFrame(tk.Frame):
    lab_base_player_stats = None
    lab_player_stats = None
    equip_inv = None

    def __init__(self, containter,state,control):
        super().__init__(containter,width=300)
        label = ttk.Label(self, text='state: [' + state + ']')
        label.grid(column=0, row=0, sticky='nsew', padx=1, pady=1)
        self.lab_base_player_stats = ttk.Label(self, text='Base Player Stats:')
        self.lab_base_player_stats.grid(column=0, row=1, sticky='nsew', padx=1, pady=1)
        self.lab_player_stats = ttk.Label(self, text='Effe Player Stats:')
        self.lab_player_stats.grid(column=0, row=2, sticky='nsew', padx=1, pady=1)
        self.equip_inv = EquipSlotFrame(self, 1, 3, control, context="Equip")
        self.equip_inv.grid(column=0, row=3, sticky='nsew', padx=1, pady=1)
        self.config(bg='green')

    def setBasePlayerStats(self, player_stats):
        self.lab_base_player_stats['text'] = str(player_stats)

    def updatePlayerStats(self, player_stats):
        self.lab_player_stats['text'] = str(player_stats)

    def updateEquipment(self, selected_items):
        self.equip_inv.updateAllEquipment(selected_items)

class EquipCellFrame(tk.Frame):
    row_number =0
    col_number =0
    feature_file = 'dummy.png'
    download_icon = None
    gameControl = None
    inv_button = None

    def __init__(self, containter,row,col, control, context):
        super().__init__(containter)
        self.gameControl = control
        self.context = context

        image = "unequipslot.png"
        self.row_number = row
        self.col_number = col
        cont_text = "{}x{}".format(self.row_number,self.col_number)
        label = ttk.Label(self, text=cont_text)
        label.grid(column=0, row=0, sticky='nsew', padx=2, pady=2)
        self.feature_file = './assets/{}'.format(image)
        self.download_icon = tk.PhotoImage(file=self.feature_file)
        self.inv_button = ttk.Button(self, image=self.download_icon, command=self.btn_clicked)
        self.inv_button.grid(column=0, row=1, sticky='nsew', padx=2, pady=2)
        self.config(bg='green')

    def clearEquipment(self):
        print("clearEquipment")
        self.feature_file = './assets/{}'.format("unequipslot.png")
        self.download_icon = tk.PhotoImage(file=self.feature_file)
        self.inv_button['image'] = self.download_icon

    def updateEquipment(self, inv_item):
        print("updateEquipment:{}".format(inv_item.imageFilename))
        self.feature_file = './assets/{}'.format(inv_item.imageFilename)
        self.download_icon = tk.PhotoImage(file=self.feature_file)
        self.inv_button['image'] = self.download_icon

    def receiveResponse(self, resp):
        #todo: pass response to cell feature for reaction and passing to game controller
        print('Response Received: {}'.format(len(resp.getResponseData())))

    def btn_clicked(self):
        print('Clicked On: {}'.format(self.feature_file))
        #todo: tell asociated feature of an intial interaction.
        #for now, create mock Dialog and pass to game controller
        #d = Dialog('Please Feed Me!{}-{}'.format(self.row_number,self.col_number),[(1,'No'),(2,'Sure'),(3,'Feed Yourself!')])
        #self.gameControl.selectInventoryItem(self.invItem)


class EquipSlotFrame(tk.Frame):
    row_number = 0
    col_number = 0
    gameControl = None
    item = None
    context = ""
    equip_cells = []

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
                cellFrame = EquipCellFrame(self, r, c, self.gameControl, self.context)
                cellFrame['bg'] = 'green'
                cellFrame.grid(column=c, row=r, sticky='nsew')
                self.equip_cells.append(cellFrame)

    def updateAllEquipment(self,items_selected):
        for cell in self.equip_cells:
            cell.clearEquipment()
        count = 0
        for key in items_selected:
            item = items_selected[key]
            self.equip_cells[count].updateEquipment(item)
            count += 1