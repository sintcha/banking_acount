from tkinter import BooleanVar, StringVar
from tkinter import messagebox

from Model.Admin import Admin
from Model.Customer import Customer


class LoginController:
    def __init__(self, view, user):
        self.view = view
        self.user = user
        self.mail = StringVar()
        self.password = StringVar()
        self.checkbox = BooleanVar()
        self.configControl()

    def configControl(self):
        self.view.mail.config(textvariable=self.mail)
        self.view.password.config(textvariable=self.password)
        self.view.admin.config(variable=self.checkbox)

    def valideEmail(self):
        return self.mail.get() != ""

    def validePassword(self):
        return self.password.get() != ""

    def onButtonValidationClicked(self):
        if self.valideEmail() and self.validePassword():
            self.user.mail = self.mail.get()
            self.user.password = self.password.get()
            if self.user.exist():
                if self.checkbox.get():
                    if self.user.isAdmin():
                        self.user.connect(True)
                        admin = Admin(self.user)
                        self.view.master.connectAdmin(admin)
                    else:
                        messagebox.showerror(title="Bad Entry", message="This admin account does not exist")

                else:
                    self.user.connect(False)
                    customer = Customer(self.user)
                    self.view.master.connectCustomer(customer)

            else:
                messagebox.showerror(title="Bad Entry",message="Error wrong email or password ")

        else:
            messagebox.showerror(title="Bad Entry", message="Error wrong email or password ")
