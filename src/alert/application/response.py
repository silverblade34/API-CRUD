

class AlertResponse():

    @staticmethod
    def parsedAlertList(raw):
        listaf = []
        print(raw)
        for row in raw:
            lista = {}
            lista['id'] = row[0]
            lista['evento'] = row[1]
            lista['descripcion'] = row[2]
            lista['placa'] = row[3]
            lista['estado'] = row[4]
            listaf.append(lista)
        message = "Ok"
        return listaf, message

    @staticmethod
    def parsedSeekList(raw):
        listaf = []
        for row in raw:
            lista = {}
            lista['id'] = row[0]
            lista['evento'] = row[1]
            lista['descripcion'] = row[2]
            lista['placa'] = row[3]
            lista['estado'] = row[4]
            listaf.append(lista)
        message = "Ok"
        return listaf, message

    @staticmethod
    def parsedCreate(raw):
        if len(raw) != 0:
            placa = {}
            placa['placa']=raw
            message = "Alerta creada con exito"
            return placa, message
        else:
            raise Exception("Alerta no encontrada")

    @staticmethod
    def parsedEdit(raw):
        if len(raw) != 0:
            placa = {}
            placa['placa']=raw
            message = "Alerta editada con exito"
            return placa, message
        else:
            raise Exception("Alerta no encontrada")

    @staticmethod
    def parsedDelete(raw):
        if len(raw) != 0:
            placa = {}
            placa['placa']=raw
            message = "Alerta eliminada con exito"
            return placa, message
        else:
            raise Exception("Alerta no encontrada")
