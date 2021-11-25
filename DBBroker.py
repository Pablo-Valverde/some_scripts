import pyodbc

_instance = None

class DBBroker:

    def __init_connection__(self, connection_string) -> None:
        conn = pyodbc.connect(connection_string)
        self.cursor = conn.cursor()

    def Read(self, sql):
        return self.cursor.execute(sql)

    def Delete(self, sql):
        return self.cursor.execute(sql).rowcount

    def Update(self, sql):
        return self.cursor.execute(sql).rowcount
        
def GetBroker():
    global _instance

    if _instance == None:   
        _instance = DBBroker()
    return _instance

def InitBroker(dbb_path, driver = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"):
    global _instance

    GetBroker()
    _instance.__init_connection__(driver + r"Dbq=" + dbb_path + r";")
