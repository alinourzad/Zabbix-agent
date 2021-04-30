#!/usr/bin/env python
"""add the two environment vars in code/.env file
   one ip="ip address" and the other hostname="hostname"
   if these two didn't exist this script will not run correctly.
"""
# we import this Host class so we can work with host on zabbix server
from code.host import Host

# to be able  to work dotenv files we use this package
import dotenv

if __name__ == "__main__":
    # get the ip from dotenv file in code/.env
    ip = dotenv.get_key("code/.env", "ip")
    # get the hostname from dotenv file in code/.env
    hostname = dotenv.get_key("code/.env", "hostname")
    # lets check if we were successful to get the keys from code/.env
    if ip is None:
        exit()
    if hostname is None:
        exit()
    # lookup code/host.py about how to use this class.
    # lets try to add/remove/... to the zabbix-server
    mongo = Host(ip, hostname)
    print(mongo.payload)
