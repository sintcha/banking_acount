from tkinter import Frame, Label, Button

from View.View import View


class ListUsersView(View):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.controller = None
        self.currentline = 1
        self.columnnum = 9
        self.buttonCancel = Button(self,text="Cancel")

    def placeElements(self):

        self.addLine(["Id","Name","Firstname","Email","Address","Phone Number","Is Admin","Balance"])
        for infos in self.controller.listUsers():
            self.addLine(infos)
        self.buttonCancel.grid(row = self.currentline,column = int(self.columnnum/2), sticky="ew")
        self.master.resizable(False,False)


    def configEvents(self):
        self.buttonCancel.config(command=lambda: self.controller.onButtonCancelClicked())

    def addLine(self,infos):
        for i in range(len(infos)):
            label = Label(self,text=infos[i])
            label.grid(row = self.currentline, column = i,sticky="ew")
            label.config(borderwidth=5, relief="groove")
        self.currentline+=1