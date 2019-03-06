from pprint import pprint
import time
import json
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def add_rule(file_name):
    files = {'topics': open('rules/' + file_name,'r')}
    r=requests.post(url + '/topics/', auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json'}, verify=False, files=files)
    print 'loaded healthbot rule ' + file_name

def add_playbook(file_name):
    files = {'playbooks': open('playbooks/' + file_name,'r')}
    r=requests.post(url + '/playbooks/', auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print 'loaded healthbot playbook ' + file_name

def add_device(dev):
    payload=json.dumps(dev)
    r = requests.post(url + '/device/' + dev['device-id'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the device: ' + dev['device-id']

def add_device_group(group):
    payload=json.dumps(group)
    r = requests.post(url + '/device-group/' + group['device-group-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the device group: ' + group['device-group-name']

def add_network_group(group):
    payload=json.dumps(group)
    r = requests.post(url + '/network-group/' + group['network-group-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the network group: ' + group['network-group-name']

def commit():
    r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print 'healthbot configuration commited!'


# update this section with your healthbot ip address
server = "172.30.52.250"
authuser = "lab"
authpwd = "m0naco"
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

# update this section with your devices details

devices = """[
    {
        "device-id": "ex4300-9",
        "host": "172.30.179.95",
        "authentication": {
            "password": {
                "username": "pytraining",
                "password": "Poclab123"
            }
        }
    },
    {
        "device-id": "ex4300-17",
        "host": "172.30.179.73",
        "authentication": {
            "password": {
                "username": "pytraining",
                "password": "Poclab123"
            }
        }
    },
    {
        "device-id": "ex4300-18",
        "host": "172.30.179.74",
        "authentication": {
            "password": {
                "username": "pytraining",
                "password": "Poclab123"
            }
        }
    }
]"""


# update this section with your device group details
device_group = """{
                "device-group-name" : "EX",
                "description" : "EX devices",
                "devices" : ["ex4300-17", "ex4300-18", "ex4300-9"],
                "playbooks" : ["collect-lldp"],
                "variable" : [
                {
                    "instance-id" : "collect-lldp-instance-1",
                    "playbook" : "collect-lldp",
                    "rule" : "lldp/collect-lldp"
                }
                ]
            }"""

# update this section with your device group details

network_group = """{
                "network-group-name" : "LLDP",
                "description" : "validate LLDP topology",
                "playbooks" : ["check-lldp"],
                "variable" : [
                {
                    "instance-id" : "ex4300-9---ex4300-17",
                    "playbook" : "check-lldp",
                    "rule" : "lldp/check-lldp",
                    "variable-value" : [
                    {
                        "name" : "devicegroup",
                        "value" : "EX"
                    },
                    {
                        "name" : "localname",
                        "value" : "ex4300-9"
                    },
                    {
                        "name" : "localport",
                        "value" : "ge-0/0/0"
                    },
                    {
                        "name" : "remotename",
                        "value" : "ex4300-17"
                    },
                    {
                        "name" : "remoteport",
                        "value" : "ge-0/0/0"
                    }
                    ]
                },
                {
                    "instance-id" : "ex4300-9---ex4300-18",
                    "playbook" : "check-lldp",
                    "rule" : "lldp/check-lldp",
                    "variable-value" : [
                    {
                        "name" : "devicegroup",
                        "value" : "EX"
                    },
                    {
                        "name" : "localname",
                        "value" : "ex4300-9"
                    },
                    {
                        "name" : "localport",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "remotename",
                        "value" : "ex4300-18"
                    },
                    {
                        "name" : "remoteport",
                        "value" : "ge-0/0/0"
                    }
                    ]
                },
                {
                    "instance-id" : "ex4300-17---ex4300-18",
                    "playbook" : "check-lldp",
                    "rule" : "lldp/check-lldp",
                    "variable-value" : [
                    {
                        "name" : "devicegroup",
                        "value" : "EX"
                    },
                    {
                        "name" : "localname",
                        "value" : "ex4300-17"
                    },
                    {
                        "name" : "localport",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "remotename",
                        "value" : "ex4300-18"
                    },
                    {
                        "name" : "remoteport",
                        "value" : "ge-0/0/1"
                    }
                    ]
                }
                ]
            }"""


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

add_rule('collect-lldp.rule')

add_playbook('collect-lldp.playbook')

my_devices=yaml.load(devices)
for item in my_devices:
    add_device(item)

my_group=yaml.load(device_group)
add_device_group(my_group)

commit()

print 'wait 6 sec'
time.sleep(6)

add_rule('check-lldp.rule')

add_playbook('check-lldp.playbook')

my_network_group=yaml.load(network_group)
add_network_group(my_network_group)

commit()

