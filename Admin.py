from Model.User import User


class Admin(User):

    def __init__(self,user = None):
        User.__init__(self,user)


    def connect(self):
        pass

    def isAdmin(self):
        return True

    def exist(self):
        return True
