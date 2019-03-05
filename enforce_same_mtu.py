from pprint import pprint
import time
import json
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def add_function(file_name):
    files = {'up_file': open('functions/' + file_name,'r')}
    r=requests.post(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False,
 files=files)
    print 'loaded healthbot function ' + file_name

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
            "instance-id" : "collect-mtu-instance-1",
            "playbook" : "collect-mtu",
            "rule" : "interfaces/collect-interfaces-mtu",
            "variable-value" : [
            {
                "name" : "interface-name-variable",
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
            "instance-id" : "collect-mtu-instance-1",
            "playbook" : "collect-mtu",
            "rule" : "interfaces/collect-interfaces-mtu",
            "variable-value" : [
            {
                "name" : "interface-name-variable",
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
            "instance-id" : "collect-mtu-instance-1",
            "playbook" : "collect-mtu",
            "rule" : "interfaces/collect-interfaces-mtu",
            "variable-value" : [
            {
                "name" : "interface-name-variable",
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
            "instance-id" : "collect-mtu-instance-1",
            "playbook" : "collect-mtu",
            "rule" : "interfaces/collect-interfaces-mtu",
            "variable-value" : [
            {
                "name" : "interface-name-variable",
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
            "instance-id" : "collect-mtu-instance-1",
            "playbook" : "collect-mtu",
            "rule" : "interfaces/collect-interfaces-mtu",
            "variable-value" : [
            {
                "name" : "interface-name-variable",
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
            "instance-id" : "collect-mtu-instance-1",
            "playbook" : "collect-mtu",
            "rule" : "interfaces/collect-interfaces-mtu",
            "variable-value" : [
            {
                "name" : "interface-name-variable",
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
            "instance-id" : "collect-mtu-instance-1",
            "playbook" : "collect-mtu",
            "rule" : "interfaces/collect-interfaces-mtu",
            "variable-value" : [
            {
                "name" : "interface-name-variable",
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
                "playbooks" : ["collect-mtu"],
                "variable" : [
                {
                    "instance-id" : "collect-mtu-instance-1",
                    "playbook" : "collect-mtu",
                    "rule" : "interfaces/collect-interfaces-mtu"
                }
                ]
            }"""

# update this section with your device group details

network_group = """{
                "network-group-name" : "MTU",
                "description" : "compare mtu",
                "playbooks" : ["compare-mtu"],
                "variable" : [
                {
                    "instance-id" : "vMX1-ge000-vMX4-ge000",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/0"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX1"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/0"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX4"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX1-ge001-vMX5-ge000",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX1"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/0"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX5"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX1-ge002-vMX6-ge000",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/2"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX1"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/0"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX1-ge003-vMX7-ge000",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/3"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX1"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/0"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX2-ge000-vMX4-ge001",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/0"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX4"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX2-ge001-vMX5-ge001",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX5"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX2-ge002-vMX6-ge001",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/2"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX2-ge003-vMX7-ge001",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/3"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX3-ge000-vMX4-ge002",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/0"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/2"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX4"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX3-ge001-vMX5-ge002",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/1"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/2"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX5"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX3-ge002-vMX6-ge002",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/2"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/2"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    }
                    ]
                },
                {
                    "instance-id" : "vMX3-ge003-vMX7-ge002",
                    "playbook" : "compare-mtu",
                    "rule" : "interfaces/compare-interfaces-mtu",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-inter-variable",
                        "value" : "ge-0/0/3"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-inter-variable",
                        "value" : "ge-0/0/2"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    }
                    ]
                }                
                ]
            }"""


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

add_rule('collect-interfaces-mtu.rule')

add_playbook('collect-mtu.playbook')

my_devices=yaml.load(devices)
for item in my_devices:
    add_device(item)

my_group=yaml.load(device_group)
add_device_group(my_group)

commit()

print 'wait 60 sec'
time.sleep(60)

add_function('change-mtu-config.py')

add_rule('compare-interfaces-mtu.rule')

add_playbook('compare-mtu.playbook')

my_network_group=yaml.load(network_group)
add_network_group(my_network_group)

commit()

