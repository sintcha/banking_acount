from tkinter import *
from tkinter import simpledialog

from View.View import View


class AdminView(View):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.controller = None
        self.buttonShowAccounts = Button(self, text="Show Customers",bg="#0F9DB0")
        self.buttonAddCustomer = Button(self, text="Add Customer",bg="#0F9DB0")
        self.buttonDeleteAccount = Button(self, text="Delete Customer",bg="#0F9DB0")

    def placeElements(self):
        self.master.title("Admin Page")
        self.buttonShowAccounts.grid(row=1, sticky='ew')
        self.buttonAddCustomer.grid(row=2, sticky='ew')
        self.buttonDeleteAccount.grid(row=3, sticky='ew')

    def configEvents(self):
        self.buttonShowAccounts.config(command=lambda: self.controller.onButtonShowClicked())
        self.buttonAddCustomer.config(command=lambda: self.controller.onButtonAddClicked())
        self.buttonDeleteAccount.config(command=lambda: self.controller.onButtonDeleteClicked())

    def askDeleteConfirmation(self):
        return simpledialog.askinteger("Delete User",prompt="Enter user Id")