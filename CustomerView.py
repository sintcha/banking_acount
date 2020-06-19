from tkinter import *
from tkinter import simpledialog, messagebox

from View.View import View


class CustomerView(View):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.controller = None
        self.label = Label(self)
        self.buttonDeposit = Button(self, text="MAKE A DEPOSIT")
        self.buttonWithdraw = Button(self, text="MAKE A WITHDRAW")
        self.buttonBalance = Button(self, text="SHOW MY BALANCE")
        self.buttonDelete = Button(self, text="DELETE MY ACCOUNT")
        self.buttonDisconnect = Button(self, text="DISCONNECT")

    def placeElements(self):
        self.master.title("Customer")
        self.label.config(text="You are connected as " + self.controller.customer.name)
        self.buttonDeposit.grid(row=0, sticky='ew')
        self.buttonWithdraw.grid(row=1, sticky='ew')
        self.buttonBalance.grid(row=2, sticky='ew')
        self.buttonDelete.grid(row=3, sticky='ew')
        self.buttonDisconnect.grid(row=4, sticky='ew')

    def configEvents(self):
        self.buttonDeposit.config(command=lambda: self.controller.onButtonDepositClicked())
        self.buttonWithdraw.config(command=lambda: self.controller.onButtonWithdrawClicked())
        self.buttonBalance.config(command=lambda: self.controller.onButtonBalanceClicked())
        self.buttonDelete.config(command=lambda: self.controller.onButtonDeleteClicked())
        self.buttonDisconnect.config(command=lambda: self.controller.onButtonDisconnectClicked())

    def askDeposit(self):
        return simpledialog.askfloat(title="Deposit",prompt="Enter value",minvalue=0)

    def askWithdraw(self):
        return simpledialog.askfloat(title="Withdraw", prompt="Enter value", minvalue=0)

    def showUpdateMessage(self):
        messagebox.showinfo(title="Info", message="Your balance will be updated at your next connexion")

    def showBalance(self,balance):
        messagebox.showinfo(title="Balance", message="Your balance is " + str(balance))

    def askDeleteConfirmation(self):
        return messagebox.askyesno(title="Confirmation",message= "Do you really want to delete your account?")

    def showDeleteConfirmation(self):
        messagebox.showinfo(title="Info", message="Your account has been deleted")