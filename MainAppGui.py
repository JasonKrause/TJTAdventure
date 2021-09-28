import tkinter as tk
from tkinter import ttk
from Control import GameController
from MapCellManagement import MapCellFrame
from UserViewManagement import UserFrame
from ObjectiveViewManagement import ObjectiveFrame
from StatusViewManagement import StatusFrame
from InventoryViewManagement import InventoryFrame
from DialogViewManagement import DialogFrame

class GridMapFrame(tk.Frame):
    gameControl = None
    def __init__(self, containter, control):
        super().__init__(containter)
        self.gameControl = control
        rows = 5
        cols = 10
        for r in range(rows):
            self.grid_rowconfigure(r, minsize=50,weight=1)
            for c in range(cols):
                self.grid_columnconfigure(c, minsize=45, weight=1)
                cellFrame = MapCellFrame(self, r,c,self.gameControl)
                cellFrame['bg']= 'green'
                cellFrame.grid(column=c,row=r, sticky='nsew')
        #label = ttk.Label(self, text='M')
        #label.grid(column=0, row=0, sticky='nsew', padx=2, pady=2)
        #self.config(bg='green')

class MapFrame(tk.Frame):
    gameControl = None
    def __init__(self, containter,title,control):
        super().__init__(containter)
        self.gameControl = control
        label = ttk.Label(self, text='map: [' + title + ']')
        label.grid(column=0, row=0, sticky=tk.NW, padx=1, pady=1)
        self.config(bg='green')
        map = GridMapFrame(self,self.gameControl)
        map.grid(column=0, row=1, sticky='nsew', padx=1, pady=1)


class App(tk.Tk):
    controller = None
    def __init__(self):
        super().__init__()
        self.controller = GameController()

        self.title("Simple Adventure Game")
        window_width = 800
        window_height = 600

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        top_frame = tk.Frame(self, bg='cyan', width=450, height=150, pady=3)
        center = tk.Frame(self, bg='gray2', width=50, height=400, padx=13, pady=13)
        btm_frame = tk.Frame(self, bg='lavender', width=450, height=160, pady=3)

        # layout all of the main containers
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)
        center.grid_columnconfigure(0, minsize=150,weight=0)#
        center.grid_columnconfigure(2, minsize=150,weight=0)#
        #top_frame.grid_rowconfigure(0, weight=1)

        #make 2nd column expand to fill remaining space
        top_frame.grid_columnconfigure(1, weight=1)
        top_frame.grid_columnconfigure(0, minsize=250,weight=0)#

        btm_frame.grid_rowconfigure(0, minsize=100,weight=0)#
        btm_frame.grid_columnconfigure(0,weight=1)#

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")

        uFrame = UserFrame(top_frame, 'dummy_user')
        uFrame['bg']= 'red'
        uFrame.grid(column=0,row=0, sticky='nsew')

        oFrame = ObjectiveFrame(top_frame, 'the objective')
        oFrame['bg']= 'green'
        oFrame.grid(column=1,row=0, sticky='nsew')

        sFrame = StatusFrame(center, 'the state')
        sFrame['bg']= 'yellow'
        #sFrame['width']=200
        sFrame.grid(column=0,row=0, sticky='nsew')

        mFrame = MapFrame(center, 'map title',self.controller)
        mFrame['bg']= 'blue'
        mFrame.grid(column=1,row=0, sticky='nsew')

        iFrame = InventoryFrame(center, 'inventory title')
        iFrame['bg']= 'purple'
        iFrame.grid(column=2,row=0, sticky='nsew')

        dFrame = DialogFrame(btm_frame, 'dialog title')
        dFrame['bg']= 'brown'
        dFrame.grid(column=0,row=0, sticky='nsew')

        self.controller.setDialogGui(dFrame)
