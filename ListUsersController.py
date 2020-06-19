class ListUsersController:
    def __init__(self, view, admin):
        self.view = view
        self.admin = admin
        self.configControl()

    def configControl(self):
        pass

    def listUsers(self):
        return self.admin.listUsers()

    def onButtonCancelClicked(self):
        self.view.master.connectAdmin(self.admin)