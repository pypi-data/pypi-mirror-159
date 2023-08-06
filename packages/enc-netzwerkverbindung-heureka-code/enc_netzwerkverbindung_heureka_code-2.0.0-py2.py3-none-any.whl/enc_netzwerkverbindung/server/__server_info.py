from dataclasses import dataclass


@dataclass(frozen=True)
class ServerInfo:
    """ Kapselt die Informationen fuer den Logger des Servers """
    file__name__: str
