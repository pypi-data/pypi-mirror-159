import jwt
from random import randint

class Secury():
    _secury_key_lock = 'senha123'
    def __getattribute__(self,value):
        if not value[0] == '_':
            data = getattr(self,f'_secury_{value}',None)
            if data != None:
                try:
                    return jwt.decode(data,self._secury_key_lock,algorithms='HS256')[value]
                except:
                    return 'Você Não Tem Permissão Para Ler Esse Informação'
        return super().__getattribute__(value)

    def __setattr__(self,attr:str,value):
        if attr.startswith('_secury_'):
            print(self._secury_key_lock)
            value = jwt.encode({attr[len('_secury_'):]:value},self._secury_key_lock).decode()
            super().__setattr__(attr,value)
            return
        else:
            key =  f'k_{randint(1,10000)}'
            if getattr(self,f'_secury_{attr}',key) != key:
                value = jwt.encode({attr:value},self._secury_key_lock).decode()
                super().__setattr__(f'_secury_{attr}',value)
                return
        super().__setattr__(attr,value)