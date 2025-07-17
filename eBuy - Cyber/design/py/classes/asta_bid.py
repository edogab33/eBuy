from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Any

if TYPE_CHECKING:
    from py.classes.Bid import Bid
    from py.classes.OggettoDelPost import Asta


class asta_bid:
    class _link:
        """ Link a responsabilità doppia, con gestione asimmetrica verso Bid.
        """
        _asta: Asta # imm
        _bid: Bid
        
        def __init__(self, asta: Asta, bid: Bid) -> None:
            self._asta: Asta = asta
            self._bid: Bid = bid
        
        def asta(self) -> Asta:
            return self._asta
        
        def bid(self) -> Bid:
            return self._bid
        
        def __hash__(self)->int:
            return hash( (self.asta(), self.bid()) )

        def __eq__(self, other:Any)->bool:
            if type(self) != type(other) or	hash(self) != hash(other):
                return False
            
            return (self.studente(), self.modulo()) == ( other.asta(), other.bid() )
        
        def __repr__(self):
            return f"asta_bid(asta={self.asta()}, bid={self.bid()})"