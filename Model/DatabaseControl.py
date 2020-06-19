import sqlite3


class DatabaseController:
    def __init__(self, filename="../bank.sql", database="Account"):
        self.filename = filename
        self.database = database
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()

    def addUser(self, name, firstname,password,mail,adress,phone,isAdmin):
        if self.isUser(mail,password):
            pass
        else:
            self.cursor.execute(
                "INSERT INTO {0} "
                "(name,firstname,password,mail,adress,phone,isAdmin)"
                " VALUES ('{1}','{2}','{3}','{4}','{5}','{6}', {7});".format(self.database,
                                                                                     name,
                                                                                     firstname,
                                                                                     password,
                                                                                     mail,
                                                                                     adress,
                                                                                     phone,
                                                                                     'TRUE' if isAdmin else 'FALSE'))
            self.connection.commit()

    def isUser(self,email,password):
        query = "SELECT DISTINCT name FROM {0} WHERE mail='{1}' AND password='{2}'".format(
            self.database, email, password)
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        if len(results) == 0:
            return False
        return True

    def listUsers(self,code=0):
        """
        :param code: 0 for all, 1 for users only, 2 for admins only
        :return:
        """
        condition = ""
        if code==1:
            condition = "WHERE NOT isAdmin"
        elif code==2:
            condition ="WHERE isAdmin"
        query = "SELECT id,name,firstname,mail,adress,phone,isAdmin,Balance FROM {0} ".format(self.database) + condition
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def getUserInfo(self,userId):
        pass

    def isAdmin(self, email, password):
        query = "SELECT DISTINCT name FROM {0} WHERE mail='{1}' AND password= '{2}' AND isAdmin".format(
            self.database, email, password)
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        if len(results) == 0:
            return False
        return True

    def getCustomer(self, user,isAdmin):

        condition = "AND isAdmin" if isAdmin else ""
        query = "SELECT DISTINCT id,name,firstname,mail,adress,balance FROM {0} WHERE mail='{1}' AND password= '{2}'".format(
            self.database, user.mail, user.password) + condition
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        user.id = result[0]
        user.name = result[1]
        user.firstname = result[2]
        user.mail = result[3]
        user.adress = result[4]
        user.balance = float(result[5])

    def addBalance(self,userId,value):
        query = "UPDATE {0} SET balance = {0}.balance+{2} WHERE {0}.id = {1}".format(self.database,userId,value)
        self.cursor.execute(query)
        self.connection.commit()

    def deleteCustomer(self,id):
        try:
            query = "DELETE FROM {0} WHERE id= {1}".format(self.database,id)
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def __del__(self):
        self.connection.close()

def main():
    import os
    if os.path.exists("../bank.sql"):
        os.remove("../bank.sql")
    conn = sqlite3.connect("../bank.sql")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Account ( id INTEGER PRIMARY KEY NOT NULL constraint AUTO_INCREMENT ,"
                   " name TEXT,"
                   " firstname TEXT,"
                   " mail TEXT,"
                   " adress TEXT,"
                   " phone TEXT,"
                   " password TEXT,"
                   " isAdmin BOOLEAN DEFAULT FALSE,"
                   " balance INTEGER DEFAULT 0);")
    database = DatabaseController("../bank.sql")
    database.addUser("Alice","Alicia","Bob","Alice@gmail.com","AliceCity","0600112233",True)
    database.addUser("Bob","Boby","Alice","Bob@gmail.com","BobCity","0700112233",False)
    database.addUser("Bobi","Boby","Alice","Bobi@gmail.com","BobiCity","0700112233",False)
    #database.deleteCustomer(3)
    #database.addBalance(2,-500)
    #database.listUsers()
    conn.commit()
    conn.close()





if __name__ == "__main__":
    main()