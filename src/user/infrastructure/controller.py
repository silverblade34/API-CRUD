from .mysql import MysqlUser
from ..application.response import UserResponse


class UserController:
    def __init__(self):
        self.mysql = MysqlUser()
        self.response = UserResponse()

    def buscarUsuario(self, user, pas):
        raw = self.mysql.userSeek(user,pas)
        parsedList = self.response.parsedSeekUser(raw) 
        return parsedList