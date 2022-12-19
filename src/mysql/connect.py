import mysql.connector

class ConnectionMysql:

    def __init__(self):
        self.conn = mysql.connector.connect( host='104.248.60.94', user= 'root', passwd='Sys4Log$$sa', db='db_test' )
        self.cursor = self.conn.cursor()