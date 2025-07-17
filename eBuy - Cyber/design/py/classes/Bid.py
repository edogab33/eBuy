from time import datetime


class Bid:
    _istante: datetime
    def __init__(self):
        self._istante = datetime.time.now()