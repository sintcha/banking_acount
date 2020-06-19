from tkinter import Frame


class View(Frame):
    def __init__(self):
        self.controller = None

    def placeElements(self):
        pass

    def configEvents(self):
        pass

    def load(self):
        self.placeElements()
        self.configEvents()

    def setController(self, controller):
        self.controller = controller
        self.load()