from datetime import datetime


class Cachable:
    def __init__(self, expiration: datetime, key: str, data: object):
        self.expiration = expiration
        self.key = key
        self.data = data

    @property
    def is_expired(self) -> bool:
        return self.expiration < datetime.now()
