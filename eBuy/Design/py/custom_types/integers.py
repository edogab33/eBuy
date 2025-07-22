from typing import Self, Type

class IntGEZ(int):
    def __new__(cls, v:int|float|Self) -> Self:
        if v < 0:
            raise ValueError(f"Il valore di {v} deve essere >= 0.")
        return int.__new__(cls, v)
    
    
class IntGET(IntGEZ):
    def __new__(cls, v:int|float|Self) -> Self:
        if v < 2:
            raise ValueError(f"Il valore di {v} deve essere >= 2.")
        return IntGEZ.__new__(cls, v)
    
    
class Voto(int):
    def __new__(cls, v:int|float|Self) -> Self:
        if v < 0 or v > 5:
            raise ValueError(f"Il valore di {v} deve essere compreso tra 0 e 5.")
        return int.__new__(cls, v)
    
    
def build_int_GE_class(v: int) -> Type:
    class IntGEV(int):
        def __new__(cls, x:int|float|Self) -> Self:
            if x < v:
                raise ValueError(f"Il valore di {x} deve essere >= {v}.")
            return int.__new__(cls, x)
    return IntGEV
