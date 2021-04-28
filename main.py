#!/usr/bin/env

import requests

URL = "http://82.99.215.219:65505/api_jsonrpc.php"


class Host:
    def __init__(self, ip, hostname):
        self.payload = {}
        self.payload['jsonrpc'] = '2.0'
        self.counter = 0
        self.hostid = ''
        self.ip = ip
        self.hostname = hostname

        self._login()

    def _login(self):
        self.payload['method'] = 'user.login'
        self.payload['params'] = {
                'user': 'ali',
                'password': 'ali@123'
                }
        self.payload['id'] = self.counter

        response = requests.post(URL, json=self.payload).json()
        self.payload['auth'] = response['result']

    def search(self):
        self.payload['id'] += 1
        self.payload['method'] = 'host.get'
        self.payload['params'] = {
                'filter': {
                    'ip': self.ip
                    }
                }
        response = requests.post(URL, json=self.payload).json()
        return response

    def add_one(self):
        search = self.search()
        if len(search['result']) == 0:
            self.payload['id'] += 1
            self.payload['method'] = 'host.create'
            self.payload['params'] = {
                    'host': self.hostname,
                    'groups': {'groupid': '2'},
                    'templates': {'templateid': '10001'},
                    'interfaces': {
                        'type': 1,
                        'dns': '',
                        'ip': self.ip,
                        'main': 1,
                        'port': '10050',
                        'useip': 1
                        }
                    }
            response = requests.post(URL, json=self.payload).json()
            # print(response)
            self.hostid = response['result']['hostids'][0]

    def delete(self):
        search = self.search()
        if len(search['result']) > 0:
            self.payload['id'] += 1
            self.payload['method'] = 'host.delete'
            self.payload['params'] = ['10420']
            response = requests.post(URL, json=self.payload).json()
            return response


if __name__ == "__main__":
    mongo = Host('192.168.1.233', 'mongo_supply')
    mongo.add_one()
    # delete
    # mongo.delete()
