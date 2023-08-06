from contextlib import suppress
class ValidationDict():
    def __init__(self,data,default=None):
        self._data = dict(data)
        self.default = default

    def __getitem__(self,valor):
        return self._data[valor]

    def get(self,key,type=None):
        response = self._data[key]
        if type:
            with suppress(Exception):
                return type(response)
            return self.default
        return response

    def __repr__(self) -> str:
        return f'<ValidationDict {list(self._data.keys())}>'