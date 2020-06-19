from tkinter import Frame, Label, Checkbutton, Entry, Button

from View.View import View


class RegistrationView(View):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.controller = None
        self.label = Label(self, text="Registration")
        self.nameLabel = Label(self, text="Name")
        self.firstnameLabel = Label(self, text="Firstname")
        self.passwordLabel = Label(self, text="Password")
        self.confirmationLabel = Label(self, text="Password Confirmation")
        self.mailLabel = Label(self, text="Email")
        self.addressLabel = Label(self, text="Address")
        self.phoneLabel = Label(self, text="Phone Number")
        self.name = Entry(self)
        self.firstname = Entry(self)
        self.password = Entry(self, show="*")
        self.passwordConfirmation = Entry(self, show="*")
        self.mail = Entry(self)
        self.address = Entry(self)
        self.phone = Entry(self)
        self.admin = Checkbutton(self, text="Is Admin")
        self.buttonValidation = Button(self, text="Validation")
        self.buttonCancel = Button(self, text="Cancel")

    def placeElements(self):
        self.master.title("Registration Page")
        self.label.grid(row=0, sticky="ew", columnspan =2)
        self.nameLabel.grid(row=1, column=0)
        self.name.grid(row=1, column=1)
        self.firstnameLabel.grid(row=2, column=0)
        self.firstname.grid(row=2, column=1)
        self.passwordLabel.grid(row=3, column=0)
        self.password.grid(row=3, column=1)
        self.confirmationLabel.grid(row=4, column=0)
        self.passwordConfirmation.grid(row=4, column=1)
        self.mailLabel.grid(row=5, column=0)
        self.mail.grid(row=5, column=1)
        self.addressLabel.grid(row=6, column=0)
        self.address.grid(row=6, column=1)
        self.phoneLabel.grid(row=7, column=0)
        self.phone.grid(row=7, column=1)
        self.admin.grid(row = 8, sticky ="ew",columnspan =2)
        self.buttonValidation.grid(row= 9,column = 0)
        self.buttonCancel.grid(row= 9,column = 1)

    def configEvents(self):
        self.buttonValidation.config( command = lambda : self.controller.onButtonValidationClicked())
        self.buttonCancel.config(command = lambda : self.controller.onButtonCancelClicked())
