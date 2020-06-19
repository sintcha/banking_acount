from Model.DatabaseControl import DatabaseController


class User:
    def __init__(self,user = None):
        if (user is None):
            self.databaseController = DatabaseController("bank.sql")
            self.id = ""
            self.name = ""
            self.firstname = ""
            self.password = ""
            self.mail = ""
            self.adress = ""
            self.balance = 0
        else:
            self.databaseController = user.databaseController
            self.id = user.id
            self.name = user.name
            self.firstname = user.firstname
            self.password = user.password
            self.mail = user.mail
            self.adress = user.adress
            self.balance = user.balance



    def connect(self,isAdmin=False):
        self.databaseController.getCustomer(self,isAdmin)

    def disconnect(self):
        pass

    def exist(self):
        return self.databaseController.isUser(self.mail, self.password)

    def isAdmin(self):
        return self.databaseController.isAdmin(self.mail, self.password)

    def listUsers(self):
        return self.databaseController.listUsers()