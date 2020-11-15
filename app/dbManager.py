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

    def formattedCols(self, base, items, token = '\"'):
        for item in items:
            base += token
            base += item
            base += token
            base += ','

        base = base[:-1]
        return base

    def insert(self, table, cols, vals):
        if table not in self.conn.tables:
            print('Table does not exist')
            return

        if len(cols) != len(vals):
            print('Data size mismatch')
            return

        session = self.conn.session
        # statement = "INSERT into" + self.conn.keyspace + "(\"Username\",\"Email\",\"Password\") " \
        #             "VALUES ('admin','admin@gmail.com','password')"

        statement = "INSERT into " + self.conn.keyspace + '.' + table + " ("

        statement = self.formattedCols(statement, cols) + ") "

        statement += "VALUES ("
        statement = self.formattedCols(statement, vals) + ");"

        print(statement)
        try:
            session.execute(statement).one()

        except Exception as e:
            print('Error with insert',e)
            return

        print('Insert success')
        return

    def select(self, table, cols):
        if table not in self.conn.tables:
            print('Table not found')
            return

        statement = "SELECT "
        if cols == '*':
            statement += '* '
        else:
            statement += "("

            statement = self.formattedCols(statement, cols, '\"') + ") "

        statement += "FROM " + self.conn.keyspace + "." + table + ';'
        print(statement)
        session = self.conn.session
        res1 = session.execute(statement).one()
        return [x for x in res1[0]]
        # return []

if __name__ == '__main__':
    dbs = DbManager()
    table = 'Users'
    cols = ['Username', 'Email', 'Password']
    vals = ['Smaran', 'smarangk@test.com', 'password']
    res1 = dbs.select(table, cols)
    print(res1)

    dbs.insert(table, cols, vals)
    dbs.select(table, cols)

# else:
#     print("An error occurred.")
