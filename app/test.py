from app.dbManager import DbManager

def getting():
    obj = DbManager()
    table = "Research"
    col = ["ResearchTitle","ResearchDescription"]
    result = obj.select(table,col)
    return result

print(getting())