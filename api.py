import requests
from functools import partial

TRELLO_URL = 'https://trello.com/'


class TrelloAPI:
    def __init__(self, endpoints, name, apikey, parent=None):
        self._ep = endpoints
        self._arg = None
        self._parent = parent
        self._name = name
        self._apikey = apikey
        for name, content in self._ep.items():
            if name == 'METHODS':
                for method in content:
                    verb = method.lower()
                    setattr(self, verb, partial(self._api_call, verb))
            else:
                setattr(self, name,
                        TrelloAPI(self._ep[name], name, self._apikey, self))

    @property
    def _url(self):
        mypart = self._name

        if self._arg:
            mypart += '/' + self._arg

        if self._parent:
            return self._parent._url + '/' + mypart
        else:
            return mypart

    def _api_call(self, method, *args, **kwargs):
        if 'params' in kwargs:
            kwargs['params']['key'] = self._apikey
        else:
            kwargs['params'] = {'key': self._apikey}
        method = getattr(requests, method)
        return method(TRELLO_URL + self._url, *args, **kwargs)

    def __call__(self, arg):
        self._arg = str(arg)
        return self


if __name__ == '__main__':
    from endpoints import ENDPOINTS
    TrelloV1 = TrelloAPI(ENDPOINTS['TrelloV1'], '1', 'INSERT KEY HERE')
