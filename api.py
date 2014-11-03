import requests
from functools import partial
TRELLO_URL = 'https://trello.com/'

class TrelloAPI:
    def __init__(self, endpoints, name, key, parent=None, arg=None):
        self._ep = endpoints
        self._arg = str(arg) if arg else None
        self._parent = parent
        self._name = name
        self._key = key
        for name, content in self._ep.items():
            if name == 'METHODS':
                for method in content:
                    verb = method.lower()
                    setattr(self, verb, partial(self.__api_call, verb))
            else:
                setattr(self, name, partial(self.__api_part, name))

    @property
    def _url(self):
        mypart = self._name

        if self._arg:
            mypart += '/' + self._arg

        if self._parent:
            return self._parent._url + '/' + mypart
        else:
            return mypart

    def __api_part(self, name, arg=None):
        return TrelloAPI(self._ep[name], name, self._key, self, arg)

    def __api_call(self, method, *args, **kwargs):
        if 'params' in kwargs:
            kwargs['params']['key'] = self._key
        else:
            kwargs['params'] = {'key': self._key}
        method = getattr(requests, method)
        return method(TRELLO_URL + self._url, *args, **kwargs)

if __name__ == '__main__':
    from endpoints import ENDPOINTS
    TrelloV1 = TrelloAPI(ENDPOINTS['TrelloV1'], '1', 'INSERT KEY HERE')
