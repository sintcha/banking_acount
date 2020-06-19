from tkinter import StringVar, BooleanVar


class RegistrationController:
    def __init__(self, view, user):
        self.view = view
        self.user = user
        self.name = StringVar()
        self.firstname = StringVar()
        self.password = StringVar()
        self.passwordConfirmation = StringVar()
        self.mail = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.admin = BooleanVar()
        self.configControl()

    def onButtonValidationClicked(self):
        print(self.name.get())
        pass

    def onButtonCancelClicked(self):
        self.view.master.loginPage()

    def isValideName(self):
        return self.name.get() != ""

    def isValideFirstname(self):
        return self.user.firstname != ""

    def configControl(self):
        self.view.name.config(textvariable = self.name)