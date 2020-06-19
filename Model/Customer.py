from Model.User import User


class Customer(User):
    def __init__(self,user = None):
        User.__init__(self,user)


    def deposit(self,amount):
        self.databaseController.addBalance(self.id,amount)

    def balance(self):
        pass

    def delete(self):
        self.databaseController.deleteCustomer(self.id)

    def withdraw(self,amount):
        self.databaseController.addBalance(self.id,-amount)

    def transfert(self):
        pass

    def addBeneficiary(self,user):
        self.beneficiarys.append(user)

    def isAdmin(self):
        return False