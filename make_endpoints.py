#!/usr/bin/env python
from collections import defaultdict
from lxml import html
from pprint import pprint

import requests

def create_tree(endpoints):
    tree = {}
    for ep in endpoints:
        verb, path = ep
        here = tree

        cls_name = 'TrelloV' + path[0]
        here.setdefault(cls_name, {})
        here = here[cls_name]

        for p in path[1:]:
            here.setdefault(p, {})
            here=here[p]
        if not 'METHODS' in here:
            here['METHODS'] = [verb]
        else:
            here['METHODS'].append(verb)
    return tree

if __name__ == '__main__':
    ep = requests.get('https://trello.com/docs/api/index.html').content
    root = html.fromstring(ep)
    endpoints = [ep for ep in root.xpath('//a/text()')
                 if 'GET' in ep or 'POST' in ep or 'DELETE' in ep]
    leafs = [(x, [i for i in y.strip('/').split('/') if not i.startswith('[')])
             for x, y in [s.split(' ',1) for s in endpoints]]
    print('ENDPOINTS = ', end='')
    pprint(create_tree(leafs), compact=True)
