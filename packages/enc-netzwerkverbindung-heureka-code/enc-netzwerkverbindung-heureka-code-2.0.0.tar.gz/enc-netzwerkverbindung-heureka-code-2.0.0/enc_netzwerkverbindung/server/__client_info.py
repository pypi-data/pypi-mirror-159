from dataclasses import dataclass


@dataclass(frozen=True)
class ClientInfo:
    """ Kapselt die Informationen fuer den Logger des Clients """
    IP: str
    file__name__: str
