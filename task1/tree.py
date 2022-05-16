#!/usr/bin/env python3
import sys
import json
import itertools
import urllib.request
from treelib import Node, Tree

ROOT_URL = 'https://openx.com/sellers.json'
def download_json(url, name):
    print(url)
    try:
        with urllib.request.urlopen(url) as api:
            data = json.loads(api.read())
            return data
    except Exception as exc:
        print(f'{name}: {str(exc)}', file=sys.stderr)
        return []


def create_new_node(client, parent, tree, id_gen):
    if not 'name' in client.keys():
        return
    name = client['name']
    id_value = next(id_gen)
    tree.create_node(name, id_value, parent = parent)
    if client['seller_type'] != 'PUBLISHER':
        return

    url = r'https://' + client['domain'] + r'/sellers.json'
    subclients = download_json(url, name)
    # if not subclients:
    #     url = r'http://' + client['domain'] + r'/sellers.json'
    #     subclients = download_json(url, name)

    if subclients:
        for cl in subclients['sellers']:
            if cl['seller_type'] != 'PUBLISHER':
                create_new_node(cl, id_value, tree, id_gen)


def main():
    id_gen = itertools.count(1)
    tree = Tree()
    seller = download_json(ROOT_URL, 'OpenX')

    root_name = seller['contact_address']
    clients = seller['sellers']
    tree.create_node(root_name, 0)


    for cl in clients:
        name = cl['name']
        create_new_node(cl, 0, tree, id_gen)

    tree.show()


if __name__ == '__main__':
    main()
