from __future__ import annotations
from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from py.classes.Bid import Bid
    from py.classes.Utente import UtentePrivato


class bid_ut:
    """ Link a responsabilità doppia con gestione asimmetrica verso Bid.
    """
    class _link:
        _bid: Bid
        _utente_privato: UtentePrivato
        
        def __init__(self, b: Bid, up: UtentePrivato) -> None:
            self._bid: Bid = b
            self._utente_privato: UtentePrivato = up
            
        def bid(self) -> Bid:
            return self._bid
        
        def utente_privato(self) -> UtentePrivato:
            return self._utente_privato
        
        def __hash__(self)->int:
            return hash( (self.bid(), self.utente_privato()) )

        def __eq__(self, other: Any)->bool:
            if type(self) != type(other) or	hash(self) != hash(other):
                return False
            
            return (self.bid(), self.utente_privato()) == ( other.bid(), other.utente_privato() )
        
        def __repr__(self):
            return f"bid_ut(bid={self.bid()}, utente_privato={self.utente_privato()})"