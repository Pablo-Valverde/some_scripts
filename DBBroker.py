from typing import Collection
import pyodbc

_instance = None

class DBBroker:

    def __init_connection__(self, connection_string: str) -> None:
        conn = pyodbc.connect(connection_string)
        self.cursor = conn.cursor()

    def Read(self, sql: str) -> Collection:
        return self.cursor.execute(sql)

    def Delete(self, sql: str) -> int:
        return self.cursor.execute(sql).rowcount

    def Update(self, sql: str) -> int:
        return self.cursor.execute(sql).rowcount
        
def GetBroker() -> DBBroker:
    global _instance

    if _instance == None:   
        _instance = DBBroker()
    return _instance

def InitBroker(dbb_path: str) -> None:
    global _instance

    GetBroker()
    _instance.__init_connection__(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" + r"Dbq=" + dbb_path + r";")