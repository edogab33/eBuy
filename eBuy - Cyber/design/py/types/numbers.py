from typing import Self, Type

class IntGEZ(int):
    def __new__(cls, v:int|float|Self) -> Self:
        if v < 0:
            raise ValueError(f"Il valore di {v} deve essere >= 0.")
        return int.__new__(cls, v)
  
    
class RealGEZ(float):
    def __new__(cls, v: int|float|str|bool|Self) -> Self:
        n: float = super().__new__(cls, v)
        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")
    
    
class RealGZ(float):
    def __new__(cls, v: int|float|str|bool|Self) -> Self:
        n: float = super().__new__(cls, v)
        if n > 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")