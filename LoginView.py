from tkinter import *
from tkinter import Frame

from View.View import View


class LoginView(View):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.emailLabel = Label(self, text="Email")
        self.mail = Entry(self)
        self.passwordLabel = Label(self, text="Password")
        self.password = Entry(self)
        self.admin = Checkbutton(self, text="Admin mode")
        self.validationButton = Button(self, text="Login")
        self.placeElements()

    def placeElements(self):
        self.master.title("login")
        self.emailLabel.grid(column=0, row=0)
        self.mail.grid(column=1, row=0)
        self.passwordLabel.grid(column=0, row=1)
        self.password.grid(column=1, row=1)
        self.admin.grid(columnspan=2, row=2)
        self.validationButton.grid(columnspan=2,row=3)

    def configEvents(self):
        self.validationButton.config( command=lambda: self.controller.onButtonValidationClicked())

