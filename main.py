#!/usr/bin/env

import requests

if __name__ == "__main__":
    url = "http://82.99.215.219:65505/api_jsonrpc.php"
    payload = {
            'jsonrpc': '2.0'
            }
    counter = 0

    # login
    payload['method'] = 'user.login'
    payload['params'] = {
            'user': 'ali',
            'password': 'ali@123'
            }
    payload['id'] = counter

    response = requests.post(url, json=payload).json()
    token = response['result']

    # search
    payload['id'] += 1
    payload['auth'] = token
    payload['method'] = 'host.get'
    payload['params'] = {
            'filter': {
                'ip': '192.168.1.233'
                }
            }
    response = requests.post(url, json=payload).json()

    # add
    if len(response['result']) == 0:
        payload['id'] += 1
        payload['method'] = 'host.create'
        payload['params'] = {
                'host': 'mongo_supply',
                'groups': {'groupid': '2'},
                'templates': {'templateid': '10001'},
                'interfaces': {
                    'type': 1,
                    'dns': '',
                    'ip': '192.168.1.233',
                    'main': 1,
                    'port': '10050',
                    'useip': 1
                    }
                }
        response = requests.post(url, json=payload).json()

    # delete
    if len(response['result']) > 0:
        payload['id'] += 1
        payload['method'] = 'host.delete'
        payload['params'] = ['10418']
        response = requests.post(url, json=payload).json()
        print(response)
