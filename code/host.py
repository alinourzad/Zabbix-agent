#!/usr/bin/env

# two packages we need to work with
import requests  # for making requests.
import dotenv    # for working with dotenv files.

# lets set up the URL so we don't type it every time.
URL = "http://82.99.215.219:65505/api_jsonrpc.php"


class Host:
    """specify the Host to be added to zabbix server
       zabbix server URL is known and its using json-rpc api.
       we need payload to work with obviously.
       https://www.zabbix.com/documentation/current/manual/api
    """
    def __init__(self, ip, hostname):
        # the path of dotenv fileme
        self.path = "code/.env"
        # initial payload. we add to it as we go.
        # it should be json compatible.
        self.payload = {}
        self.payload['jsonrpc'] = '2.0'
        # json-rpc need an id for every request. we are
        # using this as counter for id.
        self.counter = 0
        # currently useless. but we hold the hostid so
        # so we can delete it later.
        self.hostid = ''
        # the ip of the host to be added.
        self.ip = ip
        # the hostname or visible_name of the
        # host to be added.
        self.hostname = hostname
        # this function gets the auth part of the json-rpc.
        self._login()

    def _login(self):
        """get the username and password from dotenv file and logs into
           zabbix server and then sets the auth key in the payload."""
        self.payload['method'] = 'user.login'
        self.payload['params'] = {
                'user': dotenv.get_key(self.path, "zabbix_username"),
                'password': dotenv.get_key(self.path, "zabbix_password")
                }
        self.payload['id'] = self.counter

        # print(self.payload)
        response = requests.post(URL, json=self.payload).json()
        self.payload['auth'] = response['result']

    def search(self):
        """we need to search the host in zabbix server and then return
           the result.
           we are doing this by its ip of the host. this is the only way
           to search for now"""
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
        """adds the host to zabbix server via the zabbix agent way.
           zabbix agent is the only way for now."""
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
        """deletes the host by its hostid. useless for now"""
        search = self.search()
        if len(search['result']) > 0:
            self.payload['id'] += 1
            self.payload['method'] = 'host.delete'
            self.payload['params'] = ['10420']  # hostid
            response = requests.post(URL, json=self.payload).json()
            return response
