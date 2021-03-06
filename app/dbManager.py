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

    def formattedCols(self, base, items, token='\"', calltype='select'):
        for item in items:
            if calltype == 'select' or type(item) == type(''):
                item = str(item)
                base += token
                base += item
                base += token
                base += ','

            else:
                base += str(item)
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

        statement = self.formattedCols(statement, cols, '\"') + ") "

        statement += "VALUES ("
        statement = self.formattedCols(statement, vals, '\'', 'insert') + ");"

        print(statement)
        try:
            session.execute(statement).one()

        except Exception as e:
            print('Error with insert', e)
            return

        print('Insert success')
        return

    def selectstmt(self, table, cols):
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
        return statement

    def select(self, table, cols):
        session = self.conn.session
        statement = self.selectstmt(table,cols)
        print(statement)
        res1 = session.execute(statement).all()
        return [x[0] for x in res1]
        # return []

    def selectWhere(self,table,cols, condition):
        session = self.conn.session
        statement = self.selectstmt(table, cols)
        statement = statement[:-1]
        statement += " WHERE " + condition
        statement += ';'

        print(statement)
        res1 = session.execute(statement).all()
        return [x[0] for x in res1]

    def last_entry(self, table, pk):
        statement = "SELECT MAX(\"" + pk + "\") FROM " + \
                    self.conn.keyspace + '.' + table
        print(statement)
        session = self.conn.session
        res = session.execute(statement).one()
        if res[0] is None:
            return 0
        return res[0]

    # USE only if you are sure of statement
    def custom(self, statement):
        self.conn.session.execute(statement).all()


if __name__ == '__main__':
    dbs = DbManager()
    table = 'Users'
    # cols = ['Username', 'Email', 'Password']
    # vals = ['Smaran2', 'smarangk@test.com', 'password']
    # res1 = dbs.select(table, cols)
    # print(res1)

    # dbs.insert(table, cols, vals)
    # dbs.select(table, cols)
    table = 'Research'
    cols = ['ResearchID', 'ResearchTitle', 'ResearchDescription', 'Categories']
    vals = [1, 'Interesting research about trees in my area', 'I wanted to get information about the trees in my area',
            'Trees, nature']

    # dbs.insert(table,cols,vals)
    pk = 'ResearchID'
    res2 = dbs.last_entry(table, pk)
    print(res2)
    res = dbs.select(table, cols)
    print(res)

    cols = Constants.IMAGECOLS
    table = "Images"
    cond = 'ResearchId = 1'
    print(dbs.selectWhere(table, cols, cond))

# else:
#     print("An error occurred.")
