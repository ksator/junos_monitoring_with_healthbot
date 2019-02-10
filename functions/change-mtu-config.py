# from __future__ import print_function
# import re
# import sys
from jnpr.junos.device import Device
from jnpr.junos.utils.config import Config
import requests

SERVER_USERID = 'jcluser'
SERVER_PASSWORD = 'Juniper!1'

def add_config(router,interface,mtu,**kwargs):
    r = requests.get('http://api_server:9000/api/v1/device/%s/' % router, verify=False)
    device_info = r.json()
    hostname = device_info['host']
    userid = device_info['authentication']['password']['username']
    password = device_info['authentication']['password']['password']
    dev = Device(host=hostname, user=userid, password=password, normalize=True)
    dev.open()
    cu = Config(dev)
    data = "set interfaces %s mtu %s" % (interface,mtu)
    cu.load(data, format='set')
    cu.commit()
    dev.close()
