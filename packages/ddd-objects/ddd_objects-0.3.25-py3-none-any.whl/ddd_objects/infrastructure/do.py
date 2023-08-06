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
            elif isinstance(json_dict[key], list):
                new_dict[key] = [ 
                    l.to_json() if hasattr(l, 'to_json') else l for l in json_dict[key]]
            elif isinstance(json_dict[key], dict):
                new_dict[key] = {
                    k:v.to_json() if hasattr(v, 'to_json') else v for k,v in json_dict[key].items()}
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

if __name__ =='__main__':
    class A(BaseDO):
        def __init__(self) -> None:
            self.a = 1
            super().__init__()
    
    class B(BaseDO):
        def __init__(self) -> None:
            self.b = 1
            self.c = [A(), 1]
            self.d = {'a': A()}
            super().__init__()
    b = B()
    print(b.to_json())
