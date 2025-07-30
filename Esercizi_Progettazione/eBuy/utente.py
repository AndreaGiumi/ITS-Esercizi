from tipi_dato_prog.mytypes import *

class Utente:
    _username: Username # univoco
    _registrazione: datetime

    def __init__(self, username: Username, registrazione: datetime) -> None:
        self.set_username(username)
        self._registrazione = registrazione

    def set_username(self, username: Username) -> None:
        self._username = username

    def username(self) -> Username:
        return self._username
        
    def registrazione(self) -> datetime:
        return self._registrazione
    


