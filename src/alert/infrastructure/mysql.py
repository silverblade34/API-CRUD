from ...mysql.connect import ConnectionMysql

class MysqlAlert:
    def __init__(self):
        self.connect = ConnectionMysql()

    def alertList(self):
        cursor = self.connect.cursor
        cursor.execute( "SELECT evento, descripcion FROM tb_alerts")        
        dt = cursor.fetchall()
        self.connect.conn.close()
        return dt

    def alertSeek(self, id):
        cursor = self.connect.cursor
        cursor.execute( f"SELECT * FROM tb_alerts WHERE id={id}")      
        # fetchall es para extraer datos
        dt = cursor.fetchall()
        self.connect.conn.close()
        return dt

    def alertEdit(self, id, evento, descripcion, placa, estado):
        cursor = self.connect.cursor
        cursor.execute( f"UPDATE tb_alerts SET evento='{evento}', descripcion='{descripcion}', placa='{placa}', estado='{estado}' WHERE id={id}")        
        self.connect.conn.commit()
        cursor.execute( f"SELECT placa FROM tb_alerts WHERE id={id}") 
        dt = cursor.fetchall()
        cursor.close()
        return dt

    def alertCreate(self, evento, descripcion, placa, estado):
        cursor = self.connect.cursor
        cursor.execute( f"INSERT INTO tb_alerts VALUES (null,'{evento}','{descripcion}','{placa}', '{estado}')")        
        self.connect.conn.commit()
        cursor.close()
        return placa

    def alertDelete(self, id):
        cursor = self.connect.cursor
        cursor.execute( f"SELECT placa FROM tb_alerts WHERE id={id}") 
        dt = cursor.fetchall()
        cursor.execute( f"DELETE FROM tb_alerts WHERE id={id}")        
        self.connect.conn.commit()   
        cursor.close()
        return dt