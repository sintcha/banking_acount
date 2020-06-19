from tkinter import *
from tkinter import Frame

from View.View import View


class LoginView(View):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.emailLabel = Label(self, text="Email",bg="#0F9DB0")
        self.mail = Entry(self)
        self.passwordLabel = Label(self, text="Password",bg="#0F9DB0")
        self.password = Entry(self,show ="*")
        self.admin = Checkbutton(self, text="Admin mode",bg="#0F9DB0")
        self.validationButton = Button(self, text="Login",bg="green")
        self.config(background='#0F9DB0')
        self.placeElements()

    def placeElements(self):
        self.master.title("EsieaBanking")
        #self.master.geometry("720x580")
        #self.master.minsize(500, 500)
        #self.master.config(background='#0F9DB0')
        self.master.iconbitmap("download.ico")
        self.emailLabel.grid(column=0, row=0)
        self.mail.grid(column=1, row=0)
        self.passwordLabel.grid(column=0, row=1)
        self.password.grid(column=1, row=1)
        self.admin.grid(columnspan=2, row=2)
        self.validationButton.grid(columnspan=2,row=3)

    def configEvents(self):
        self.validationButton.config( command=lambda: self.controller.onButtonValidationClicked())

