#!/usr/bin/env python
"""
APIs de Trello.

"""
from functools import partial
import inspect
import os

import requests
import yaml

__all__ = []

TRELLO_URL = 'https://trello.com/'
HERE = os.path.dirname(__file__)

with open(os.path.join(HERE, 'endpoints.yaml'), 'rb') as ep_file:
    ENDPOINTS = yaml.load(ep_file.read())

class TrelloAPI:
    """
    Clase encargada de hacer de interfaz con la API de Trello.

    Genera métodos dinámicamente que se corresponden con las distintas
    ramas de las URLs.

    Define el método __call__ para poder pasar parámetros en la URL.

    """
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
        """
        Resuelve la URL hasta este punto.

        >>> trello = TrelloAPIV1('APIKEY')
        >>> trello.batch._url
        '1/batch'
        >>> trello.boards('BOARD_ID')._url
        '1/boards/BOARD_ID'
        >>> trello.boards('BOARD_ID')('FIELD')._url
        '1/boards/BOARD_ID/FIELD'
        >>> trello.boards('BOARD_ID').cards('FILTER')._url
        '1/boards/BOARD_ID/cards/FILTER'

        """
        mypart = '/'.join(filter(None, [self._name, self._arg]))

        if self._parent:
            return '/'.join(filter(None, [self._parent._url, mypart]))
        else:
            return mypart

    def _api_call(self, method, *args, **kwargs):
        """
        Hace la petición HTTP al endpoint deseado.

        """
        if 'params' in kwargs:
            kwargs['params']['key'] = self._apikey
        else:
            kwargs['params'] = {'key': self._apikey}

        method = getattr(requests, method)

        return method(TRELLO_URL + self._url, *args, **kwargs)

    def __call__(self, arg):
        self._arg = str(arg)

        return TrelloAPI(self._ep, None, self._apikey, self)


def generate_api(version):
    """
    Genera una función que instanciará la API de la versión indicada.

    """
    def get_partial_api(key):
        return TrelloAPI(ENDPOINTS[version], version, key)

    get_partial_api.__doc__ = \
        """Interfaz REST con Trello. Versión {}""".format(version)

    return get_partial_api

#
# Generamos y registramos una clase TrelloAPI por cada versión
#
for version in ENDPOINTS.keys():
    api_cls = generate_api(version)
    api_name = 'TrelloAPIV{}'.format(version)

    # Registramos la clase en el módulo 
    globals()[api_name] = api_cls

    # Permitimos que se importe la clase con `import *`
    __all__.append(api_name)
