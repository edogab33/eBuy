from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from py.custom_types.integers import IntGEZ
from py.custom_types.floats import FloatGEZ, FloatGZ
from py.custom_types.enums import Condizioni

if TYPE_CHECKING:
    from py.classes.Bid import Bid
    from py.classes.asta_bid import asta_bid

import datetime


class OggettoDelPost(ABC):
    _descrizione: str
    _anni_garanzia: IntGEZ
    _pubblicazione: datetime
    _prezzo: FloatGEZ
    _is_nuovo: bool
    _condizioni: Condizioni
    
    @abstractmethod
    def __init__(self, 
                 descrizione: str, 
                 anni_garanzia: IntGEZ, 
                 prezzo: FloatGEZ, 
                 is_nuovo: bool, 
                 condizioni: Condizioni = None
    ) -> None:
        self.set_descrizione(descrizione)
        self.set_anni_garanzia(anni_garanzia)
        self._pubblicazione = datetime.datetime.now()
        self.set_prezzo(prezzo)
        self.set_is_nuovo(is_nuovo)
        self.set_condizioni(condizioni)
    
    def set_descrizione(self, descrizione:str) -> None:
        self._descrizione = descrizione
        
    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        self._anni_garanzia = anni_garanzia
        
    def set_prezzo(self, prezzo: FloatGEZ) -> None:
        self._prezzo = prezzo
        
    def set_is_nuovo(self, is_nuovo: bool) -> None:
        self._is_nuovo = is_nuovo
        
    def set_condizioni(self, condizioni: Condizioni) -> None:
        self._condizioni = condizioni
        
    def descrizione(self) -> str:
        return self._descrizione
    
    def anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def pubblicazione(self) -> datetime:
        return self._pubblicazione
    
    def prezzo(self) -> FloatGEZ:
        return self._prezzo
    
    def is_nuovo(self) -> bool:
        return self._is_nuovo
    
    def condizioni(self) -> Condizioni:
        return self._condizioni
    
    def __repr__(self) -> str:
        return f"OggettoDelPost(descrizione={self.descrizione()},\n \
                anni_garanzia={self.anni_garanzia()},\n \
                pubblicazione={self.pubblicazione()},\n \
                prezzo={self.prezzo()}, is_nuovo={self.is_nuovo()},\n \
                condizioni={self.condizioni()})"
        
        
class Asta(OggettoDelPost):
    _scadenza: datetime = None
    _prezzo_rialzo: FloatGEZ = None
    _bids: dict[Bid, asta_bid._link] = {}
    
    def __init__(self, 
                 *, 
                 descrizione: str, 
                 anni_garanzia: IntGEZ, 
                 prezzo: FloatGEZ, 
                 is_nuovo: bool, 
                 condizioni: Condizioni = None,
                 scadenza: datetime,
                 prezzo_rialzo: FloatGEZ
    ) -> None:
        super().__init__(
                       descrizione,
                       anni_garanzia,
                       prezzo,
                       is_nuovo,
                       condizioni
                       )
        self.set_anni_garanzia(anni_garanzia)
        self.set_descrizione(descrizione)
        self.set_prezzo_rialzo(prezzo_rialzo)
        self.set_scadenza(scadenza)
    
    def set_prezzo_rialzo(self, p: FloatGZ) -> None:
        # a evoluzione controllata
        self._prezzo_rialzo = p
    
    def set_scadenza(self, s: datetime) -> None:
        # a evoluzione controllata
        self._scadenza = s
    
    def add_bid(self, u:UtentePrivato) -> None:
        from py.classes.Bid import Bid
        Bid(asta=self, up=u)
        
    def _add_asta_bid(self, l: asta_bid) -> None:
        if l.asta() is not self:
            raise KeyError("Link does not involve me.")
        
        if l.bid() in self._bids:
            raise KeyError("Duplicate link.")
        
        self._bids[l.bid()] = l
        
    def scadenza(self) -> datetime:
        return self._scadenza
    
    def prezzo_rialzo(self) -> FloatGEZ:
        return self._prezzo_rialzo
        
    def ultimo_bid(self) -> Bid:
        max_b = self._bids[list(self._bids.keys())[0]]
        for l in self._bids.values():
            if l.bid().istante() > max_b.istante():
                max_b = l.bid()
        return max_b
    
    def conclusa(self) -> bool:
        if self.scadenza() <= datetime.now():
            return True
        return False
    
    def vincitore(self) -> UtentePrivato:
        if not self.conclusa():
            raise ValueError("L'asta non è conclusa.")
        ultimo_bid = self.ultimo_bid()
        return ultimo_bid._bid_ut_link.utente_privato()
     
    def __repr__(self):
        return f"Asta(OggettoDelPost = {super().__repr__()},\n " \
               f"scadenza = {self._scadenza},\n " \
               f"prezzo_rialzo = {self._prezzo_rialzo},\n " \
               f"bids = {self._bids})"
        
if __name__ == "__main__":
    from py.classes.Utente import UtentePrivato
    
    a = Asta(
        descrizione="Test",
        anni_garanzia=IntGEZ(1),
        prezzo=FloatGEZ(10.0),
        is_nuovo=True,
        scadenza=datetime.datetime.now(),
        prezzo_rialzo=FloatGEZ(2),
        condizioni=Condizioni("ottimo")
    )
    
    #print(a)
    
    a.add_bid(UtentePrivato("test_user"))
    
    #print("\nAfter adding a bid:")
    #print(a)
    
    print(a.ultimo_bid())
    
    print("Vincitore:", a.vincitore())