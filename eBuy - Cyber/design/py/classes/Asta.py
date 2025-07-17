from classes import PostOggetto
from types.numbers import (
    RealGZ,
    Condizione,
    IntGEZ,
    RealGEZ
)
from time import datetime


class Asta(PostOggetto):
    _prezzo_bid: RealGZ
    _scadenza: datetime
    
    def __init__(self, 
                 *,
                 prezzo: RealGEZ, 
                 anni_garanzia: IntGEZ,
                 descrizione: str,
                 is_nuovo: bool,
                 condizione: Condizione,
                 prezzo_bid: RealGZ,
                 scadenza: datetime
        ) -> None:
        
        super().__init__(
            prezzo,
            anni_garanzia,
            descrizione,
            is_nuovo,
            condizione
        )
        self.set_prezzo_bid(prezzo_bid)
        self.set_scadenza(scadenza)
        
    def set_prezzo_bid(self, p: RealGZ) -> None:
        # a evoluzione controllata
        self._prezzo_bid = p
    
    def set_scadenza(self, s: datetime) -> None:
        # a evoluzione controllata
        self._scadenza = s