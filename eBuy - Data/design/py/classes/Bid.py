from __future__ import annotations
from typing import TYPE_CHECKING, Any, Self, Tuple
from py.classes.bid_ut import bid_ut
from py.classes.asta_bid import asta_bid
from py.classes.OggettoDelPost import Asta
from py.classes.Utente import UtentePrivato

import datetime

if TYPE_CHECKING:
    from py.classes.Index import Index


class Bid:
    _istante: datetime                # imm
    _asta_bid_link: asta_bid._link    # imm, certamente noto alla nascita
    _bid_ut_link: bid_ut._link        # imm, certamente noto alla nascita
    _index:Index[Tuple[datetime.datetime, int],Self] = Index[Tuple[datetime.datetime, int],Self]('Bid')
    
    def __init__(self, *, asta: Asta, up: UtentePrivato) -> None:
        self._istante = datetime.datetime.now()
        self._add_link_asta_bid(asta)
        self._add_link_bid_ut(up)
        self._set_id(self._istante, asta.id())
        
    @classmethod
    def all(cls):
        return cls._index.all()
    
    @classmethod
    def get(cls, key:Any)->Self|None:
        return cls._index.get(key)
    
    def _set_id(self, i: datetime, asta: int) -> None:
        self._index.add((i, asta), self)
        self._id = (i, asta)
        
    def istante(self) -> datetime:
        return self._istante
    
    def bid_ut(self) -> bid_ut._link:
        return self._bid_ut_link
    
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