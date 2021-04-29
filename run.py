#!/usr/bin/env python
"""add the two environment vars in code/.env file
   one ip="ip address" and the other hostname="hostname"
   if these two didn't exist this script will not run correctly.
"""

from code.host import Host

import dotenv

if __name__ == "__main__":
    ip = dotenv.get_key("code/.env", "ip")
    hostname = dotenv.get_key("code/.env", "hostname")
    if ip is None:
        exit()
    if hostname is None:
        exit()
    # lookup code/host.py about how to use this class.
    mongo = Host(ip, hostname)
    print(mongo.payload)
