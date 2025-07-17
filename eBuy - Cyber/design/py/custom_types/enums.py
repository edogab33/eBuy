from enum import *

class Condizioni(StrEnum):
    ottimo = auto()
    buono = auto()
    discreto = auto()
    da_sistemare = auto()
    

class Popolarita(StrEnum):
    bassa = auto()
    media = auto()
    alta = auto()