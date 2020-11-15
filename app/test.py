from app.dbManager import DbManager

def getting():
    obj = DbManager()
    table = "Users"
    col = ["Username","Email"]
    result = obj.select(table,col)
    return result


print(getting())

