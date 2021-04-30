# IMPORTANT

 This repo is deprecated due to switching to golang. please fill free to
contribute and add and remove how ever you like. 

# Scenario

The goal for this application is automating, installing zabbix agent
and adding the host to the zabbix server with proper configuration. 

# How Stuff Works

 There is dotenv file in the code folder. There should be some keys 
available such as: zabbix_username, zabbix_password, ip, hostname.
 
 ip and hostname are keys for the host to be added to zabbix_server. for
adding a host to zabbix you define these keys in the code/dotenv file and
create an instance from Host class in code/host.py. when creating the 
instance you automatically login and get the token from zabbix server 
with the provided username and password keys in the dotenv. 
 
 now you can can Instance.add_one() to add the host to zabbix server.

# Condolences

 I had a plan for this repo to completely implement all features for 
automating adding and configuring host to zabbix server.
 
 now we have planned for switching go. this repo is going deprecated.

# TODO

* storage to hold the status of last host added such as hostid and the 
  configuration of it.
* list of templates and groups to hold theire groupid and templateid.

# FIX

* delete function dosen't store the hostid. There is no way to store the
  hostid and use the function. basically the Host.delete() is useless.
