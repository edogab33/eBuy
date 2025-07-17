from __future__ import annotations
from typing import TYPE_CHECKING
from abc import *
from py.custom_types.enums import Popolarita
from py.custom_types.floats import FloatGZ

import datetime

if TYPE_CHECKING:
    from py.classes.Bid import Bid
    from py.classes.bid_ut import bid_ut


class Utente(ABC):
    _username: str  # imm
    _registrazione: datetime    # imm
    
    @abstractmethod
    def __init__(self, username: str) -> None:
        self.set_username(username)
        self._registrazione = datetime.datetime.now()
    
    def set_username(self, u: str) -> None:
        self._username = u
        
    def username(self) -> str:
        return self._username
    
    def popolarita(i: datetime) -> Popolarita:
        pass
    
    def affidabilita(i: datetime) -> FloatGZ:
        pass
    
    def __repr__(self):
        return f"Utente(username={self.username()}, registrazione={self._registrazione})"
    

class UtentePrivato(Utente):
    _bid_ut_link: dict[Bid, bid_ut._link] = {}
    
    def __init__(self, username: str) -> None:
        super().__init__(username)
        
    def _add_bid_ut_link(self, l) -> None:
        if l.utente_privato() is not self:
            raise ValueError("Link does not involve me.")
        
        if l.bid() in self._bid_ut_link:
            raise KeyError("Duplicate link.")
        
        self._bid_ut_link[l.bid()] = l
        
    def __repr__(self):
        return f"UtentePrivato{super().__repr__()}"