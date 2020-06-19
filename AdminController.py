class AdminController:
    def __init__(self,view,admin):
        self.view = view
        self.admin = admin
        self.configControl()

    def configControl(self):
        pass

    def onButtonShowClicked(self):
        self.view.master.listuser(self.admin)

    def onButtonAddClicked(self):
        self.view.master.createUser()

    def onButtonDeleteClicked(self):
        pass