#Sachez que si vous voyez des modifications dans le code c'est juste pour des tests

from tkinter import *
from tkinter.font import nametofont

from Controller.ListUsersController import ListUsersController
from Controller.RegistrationController import RegistrationController
from Model.User import User
from Controller.AdminController import AdminController
from Controller.CustomerController import CustomerController
from Controller.LoginController import LoginController
from View.AdminView import AdminView
from View.CustomerView import CustomerView
from View.ListUsersView import ListUsersView
from View.LoginView import LoginView
from View.RegistrationView import RegistrationView

DEFAUlT_TEXT_SIZE = 15


class BankApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = None
        self.loginPage()

    def loginPage(self):
        self.switchFrame(LoginView, LoginController)

    def switchFrame(self, frame, controller, user = User()):
        new_frame = frame(self)
        new_frame.setController(controller(new_frame,user))
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.grid()

    def connectAdmin(self,admin):
        self.switchFrame(AdminView, AdminController, admin)

    def connectCustomer(self,customer):
        self.switchFrame(CustomerView, CustomerController, customer)

    def createUser(self):
        self.switchFrame(RegistrationView, RegistrationController)

    def listuser(self,admin):
        self.switchFrame(ListUsersView, ListUsersController, admin)


def main():
    launcher = BankApp()
    default_text = nametofont("TkTextFont")
    default_text.configure(size=DEFAUlT_TEXT_SIZE)
    default_font = nametofont("TkDefaultFont")
    default_font.configure(size=DEFAUlT_TEXT_SIZE)
    launcher.option_add("*Font", default_font)
    launcher.mainloop()


if __name__ == "__main__":
    main()