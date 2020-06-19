class CustomerController:
    def __init__(self, view, customer):
        self.view = view
        self.customer = customer
        self.configControl()


    def configControl(self):
        pass

    def onButtonDepositClicked(self):
        amount = self.view.askDeposit()
        if amount is not None:
            self.customer.deposit(amount)
            self.view.showUpdateMessage()

    def onButtonWithdrawClicked(self):
        amount = self.view.askWithdraw()
        if amount is not None:
            self.customer.withdraw(amount)
            self.view.showUpdateMessage()

    def onButtonBalanceClicked(self):
        balance = self.customer.balance
        self.view.showBalance(balance)

    def onButtonDeleteClicked(self):
        confirmation = self.view.askDeleteConfirmation()
        if confirmation == True:
            self.customer.delete()
            self.view.showDeleteConfirmation()
            self.disconnect()



    def onButtonDisconnectClicked(self):
        self.disconnect()

    def disconnect(self):
        self.view.master.loginPage()