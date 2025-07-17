from types.numbers import (
    RealGEZ,
    IntGEZ
)
from types.enums import Condizione
from time import datetime
from abc import *

class PostOggetto(ABC):
    _prezzo: RealGEZ
    _anni_garanzia: IntGEZ
    _descrizione: str
    _pubblicazione: datetime # immutabile
    _is_nuovo: bool # immutabile
    _condizione: Condizione
    
    @abstractmethod
    def __init__(self, 
                 *,
                 prezzo: RealGEZ, 
                 anni_garanzia: IntGEZ,
                 descrizione: str,
                 is_nuovo: bool,
                 condizione: Condizione
        ) -> None:
        
        self.set_prezzo(prezzo)
        self.set_anni_garanzia(anni_garanzia)
        self.set_descrizione(descrizione)
        self.set_condizione(condizione)
        self._is_nuovo = is_nuovo
        self._pubblicazione = datetime.now()
        
        
    def set_prezzo(self, p: RealGEZ) -> None:
        # a evoluzione vincolata
        self._prezzo = p
        
    def set_anni_garanzia(self, a: IntGEZ) -> None:
        # a evoluzione vincolata
        self._anni_garanzia = a
        
    def set_descrizione(self, d: str) -> None:
        self._descrizione = d
        
    def set_condizione(self, c: Condizione) -> None:
        self._condizione = c
        
    def prezzo(self) -> RealGEZ:
        return self._prezzo
    
    def anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia
    
    def descrizione(self) -> str:
        return self._descrizione
    
    def condizione(self) -> Condizione:
        return self._condizione
    
    def is_nuovo(self) -> bool:
        return self._is_nuovo
    
    def pubblicazione(self) -> datetime:
        return self._pubblicazione