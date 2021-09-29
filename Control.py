class PlayerStats:
    dex = 0;
    str = 0;
    con = 0;
    itl = 0;
    wis = 0;
    cha = 0;
    def __init__(self,dex=0, str=0, con=0, itl=0, wis=0, cha=0):
        self.dex = dex
        self.str = str
        self.con = con
        self.itl = itl
        self.wis = wis
        self.cha = cha

    def __str__(self):
        return "dex{} str{} con{} int{} wis{} cha{}".format(
            self.dex, self.str, self.con, self.itl, self.wis, self.cha)

    def modifyStats(self, modifier):
        self.dex += modifier.dex
        self.str += modifier.str
        self.con += modifier.con
        self.itl += modifier.itl
        self.wis += modifier.wis
        self.cha += modifier.cha

    def setStats(self, new_stats):
        self.dex = new_stats.dex
        self.str = new_stats.str
        self.con = new_stats.con
        self.itl = new_stats.itl
        self.wis = new_stats.wis
        self.cha = new_stats.cha

class PlayerStatsModifier:
    dex = 0;
    str = 0;
    con = 0;
    itl = 0;
    wis = 0;
    cha = 0;
    def __init__(self,dex=0, str=0, con=0, itl=0, wis=0, cha=0):
        self.dex = dex
        self.str = str
        self.con = con
        self.itl = itl
        self.wis = wis
        self.cha = cha

    def __str__(self):
        return "dex{} str{} con{} int{} wis{} cha{}".format(
            self.dex, self.str, self.con, self.itl, self.wis, self.cha)

class GameController:
    dialogGui = None
    status_gui = None
    invContextSelection = {}
    play_stats = None
    effective_player_stats = None

    def __init__(self):
        self.play_stats = PlayerStats(dex=10, cha=8, str=5)
        self.effective_player_stats = PlayerStats()
        self.effective_player_stats.setStats(self.play_stats)

    def setDialogGui(self, d):
        self.dialogGui = d

    def setStatusGui(self, g):
        self.status_gui = g

    def displayDialog(self, d, cell):
        self.dialogGui.displayDialog(d, cell)

    def selectInventoryItem(self, invItem):
        print("item selected: {}".format(invItem))
        #update items selected
        self.invContextSelection[invItem.context] = invItem
        print(self.invContextSelection)
        #recalc and update effective stats
        self.effective_player_stats.setStats(self.play_stats)
        for key in self.invContextSelection:
            item = self.invContextSelection[key]
            print(type(item))
            self.effective_player_stats.modifyStats(item.statsMod)
        self.status_gui.updatePlayerStats(self.effective_player_stats)
        self.status_gui.updateEquipment(self.invContextSelection)

    def startGameControl(self):
        self.status_gui.updatePlayerStats(self.effective_player_stats)
        self.status_gui.setBasePlayerStats(self.play_stats)


