
class GameController():
    dialogGui = None

    def setDialogGui(self,d):
        self.dialogGui = d;

    def displayDialog(self,d,cell):
        self.dialogGui.displayDialog(d,cell)

