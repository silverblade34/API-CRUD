from ...mysql.connect import ConnectionMysql
import hashlib
from hashlib import md5

class MysqlUser:
    def __init__(self):
        self.connect = ConnectionMysql()
    
    def userSeek(self, user, pas):
         cursor = self.connect.cursor
         print(user)
         print(pas)
         m = hashlib.md5()
         m.update(pas.encode('utf-8'))  
         print(m.hexdigest())
         cursor.execute(f"SELECT state, token FROM tb_user WHERE usuario='{user}' AND password='{m.hexdigest()}'")      
         # fetchall es para extraer datos
         dt = cursor.fetchall()
         self.connect.conn.close()
         print(dt)
         return dt