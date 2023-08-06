from typing import Optional
from time import time

try:
    from sqlalchemy.ext.declarative import declarative_base
    SQLALCHEMY_ENV = True
except:
    SQLALCHEMY_ENV = False

if SQLALCHEMY_ENV:
    SqlalchemyBase = declarative_base()

class BaseDO:
    def to_json(self):
        json_dict = vars(self)
        new_dict = {}
        for key in json_dict:
            if hasattr(json_dict[key], 'to_json'):
                new_dict[key] = json_dict[key].to_json()
            else:
                new_dict[key] = json_dict[key]
        return new_dict

    def from_json(self):
        raise NotImplementedError

class ExpiredDO(BaseDO):
    def __init__(self, life_time:Optional[int]=None) -> None:
        self.life_time = life_time
        if self.life_time is None:
            self.expired_time = None
        else:
            self.expired_time = time()+self.life_time

    @property
    def is_expired(self):
        if self.expired_time is None:
            return False
        else:
            return self.expired_time<time()        
