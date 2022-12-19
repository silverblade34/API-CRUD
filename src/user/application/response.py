class UserResponse():

    @staticmethod
    def parsedSeekUser(raw):
        lista = {}
        if len(raw) != 0:
            for row in raw:
                lista['state'] = bool(row[0])
                lista['token'] = row[1]
            message = "Ok"
        else:
            raise Exception("Usuario invalido")

        return lista, message