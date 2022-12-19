from .mysql import MysqlAlert
from ..application.response import AlertResponse


class AlertsController:
    def __init__(self):
        self.mysql = MysqlAlert()
        self.response = AlertResponse()

    def listarAlertas(self):
        raw = self.mysql.alertList()
        parsedList = self.response.parsedAlertList(raw)
        return parsedList

    def buscarAlertas(self, id):
        raw = self.mysql.alertSeek(id)
        parsedList = self.response.parsedSeekList(raw)
        return parsedList

    def editarAlertas(self, id, evento, descripcion, placa, estado):
        raw = self.mysql.alertEdit(id, evento, descripcion, placa, estado)
        parsedList = self.response.parsedEdit(raw)  
        return parsedList

    def crearAlertas(self,evento, descripcion, placa, estado):
        raw = self.mysql.alertCreate(evento, descripcion, placa, estado)
        parsedList = self.response.parsedCreate(raw) 
        return parsedList

    def eliminarAlertas(self, id):
        raw = self.mysql.alertDelete(id) 
        parsedList= self.response.parsedDelete(raw)
        return parsedList