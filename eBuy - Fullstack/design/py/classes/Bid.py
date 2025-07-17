from py.classes.bid_ut import bid_ut
from py.classes.asta_bid import asta_bid
from py.classes.OggettoDelPost import Asta
from py.classes.Utente import UtentePrivato

import datetime


class Bid:
    _istante: datetime                # imm
    _asta_bid_link: asta_bid._link    # imm, certamente noto alla nascita
    _bid_ut_link: bid_ut._link        # imm, certamente noto alla nascita
    
    def __init__(self, *, asta: Asta, up: UtentePrivato) -> None:
        self._istante = datetime.datetime.now()
        self._add_link_asta_bid(asta)
        self._add_link_bid_ut(up)
        
    def istante(self) -> datetime:
        return self._istante
    
    def _add_link_asta_bid(self, asta: Asta) -> None:
        l = asta_bid._link(asta, self)
        self._asta_bid_link = l
        asta._add_asta_bid(l)
        
    def _add_link_bid_ut(self, up: UtentePrivato) -> None:
        l = bid_ut._link(self, up)
        self._bid_ut_link = l
        up._add_bid_ut_link(l)
        
    def __repr__(self) -> str:
        return f"Bid(istante={self.istante()},\n \
                utente_privato={self._bid_ut_link.utente_privato()},\n \
                asta={self._asta_bid_link.asta()})"