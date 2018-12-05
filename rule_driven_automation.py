import json
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def add_function(file_name):
    files = {'up_file': open('functions/' + file_name,'r')}
    r=requests.post(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print 'loaded healthbot function ' + file_name
#    return r.status_code

def add_rule(file_name):
    files = {'topics': open('rules/' + file_name,'r')}
    r=requests.post(url + '/topics/', auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json'}, verify=False, files=files)
    print 'loaded healthbot rule ' + file_name
#    return r.status_code

def add_playbook(file_name):
    files = {'playbooks': open('playbooks/' + file_name,'r')}
    r=requests.post(url + '/playbooks/', auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print 'loaded healthbot playbook ' + file_name 
#    return r.status_code

def add_device(dev):
    payload=json.dumps(dev)
    r = requests.post(url + '/device/' + dev['device-id'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the device: ' + dev['device-id']
#    return r.status_code

def add_device_group(group):
    payload=json.dumps(group)
    r = requests.post(url + '/device-group/' + group['device-group-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the device group: ' + group['device-group-name']
#    return r.status_code

def commit():
    r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print 'healthbot configuration commited!'
 #   return r.status_code


# update this section with your healthbot ip address
server = "100.123.35.0"
authuser = "jcluser"
authpwd = "Juniper!1"
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

# update this section with your devices details

devices = """[
    {
        "device-id": "vMX1",
        "host": "100.123.1.0",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2|ge-0/0/3"
            }
            ]
        }
        ]
    },
    {
        "device-id": "vMX2",
        "host": "100.123.1.1",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2|ge-0/0/3"
            }
            ]
        }
        ]
    },
    {
        "device-id": "vMX3",
        "host": "100.123.1.2",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2|ge-0/0/3"
            }
            ]
        }
        ]
    },
    {
        "device-id": "vMX4",
        "host": "100.123.1.3",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2"
            }
            ]
        }
        ]
    },
    {
        "device-id": "vMX5",
        "host": "100.123.1.4",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2"
            }
            ]
        }
        ]
    },
    {
        "device-id": "vMX6",
        "host": "100.123.1.5",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2"
            }
            ]
        }
        ]
    },
    {
        "device-id": "vMX7",
        "host": "100.123.1.6",
        "open-config": {
            "port": 32768
        },
        "authentication": {
            "password": {
                "username": "jcluser",
                "password": "Juniper!1"
            }
        },
        "variable" : [
        {
            "instance-id" : "enforce-int-state-instance-1",
            "playbook" : "enforce-int-state",
            "rule" : "interfaces/enforce-interfaces-state",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2"
            }
            ]
        }
        ]
    }
]"""


# update this section with your device group details
device_group = """{
                "device-group-name" : "vmx",
                "description" : "vmx",
                "devices" : ["vMX1", "vMX2", "vMX3", "vMX4", "vMX5", "vMX6", "vMX7"],
                "playbooks" : ["enforce-int-state"],
                "variable" : [
                {
                    "instance-id" : "enforce-int-state-instance-1",
                    "playbook" : "enforce-int-state",
                    "rule" : "interfaces/enforce-interfaces-state"
                }
                ]
            }"""

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

add_function('enable_a_disabled_interface.py')

add_rule('enforce-interfaces-state.rule')

add_playbook('enforce-int-state.playbook')

my_devices=yaml.load(devices)
for item in my_devices:
    add_device(item)

my_group=yaml.load(device_group)
add_device_group(my_group)

commit()


