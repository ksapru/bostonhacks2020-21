# row = session.execute("CREATE TABLE user").one()
import os
import dbconnect
from config import Constants

class DbManager:
    def __init__(self):
        pwd = os.getcwd()
        os.chdir(Constants.BASEDIR)
        self.conn = dbconnect.DB()
        os.chdir(pwd)

    def insert(self,table,cols,vals):
        if table not in self.conn.tables:
            print('Table does not exist')
            return

        if len(cols) != len(vals):
            print('Data size mismatch')
            return

        session = self.conn.session
        # statement = "INSERT into" + self.conn.keyspace + "(\"Username\",\"Email\",\"Password\") " \
        #             "VALUES ('admin','admin@gmail.com','password')"

        statement =  "INSERT into" + self.conn.keyspace + " ("
        for col in cols:
            statement += '\"'
            statement += col
            statement += '\",'

        statement = statement[:-1] + ")"

        print(statement)
        res = session.execute(statement).one()

    def select(self, table, cols):
        if table not in self.conn.tables:
            print('Table not found')
            return

        statement = "SELECT "
        if cols == '*':
            statement += '* '
        else:
            statement += "("
            for col in cols:
                statement += '\"'
                statement += col
                statement += '\",'
            statement = statement[:-1] + ") "

        statement += "FROM " + self.conn.keyspace + "." + table + ';'
        session = self.conn.session
        res1 = session.execute(statement).one()
        return [x for x in res1]

if __name__ == '__main__':
    dbs = DbManager()
    table = 'Users'
    cols = ['Username', 'Email']
    res1 = dbs.select(table,cols)
    print(res1)

# else:
#     print("An error occurred.")