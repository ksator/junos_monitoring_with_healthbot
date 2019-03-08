import json
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def add_tables_and_views(file_name):
    files = {'up_file': open('tables_and_views/' + file_name,'r')}
    r=requests.post(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print 'loaded healthbot table and view ' + file_name

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

def commit():
    r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print 'healthbot configuration commited!'


device_group = """{
                "device-group-name" : "vmx",
                "description" : "vmx",
                "devices" : ["vMX1", "vMX2", "vMX3", "vMX4", "vMX5", "vMX6", "vMX7"],
                "playbooks" : ["bgp-using-openconfig", "interfaces-using-openconfig", "inventory"],
                "variable" : [
                {
                    "instance-id" : "bgp-instance-1",
                    "playbook" : "bgp-using-openconfig",
                    "rule" : "bgp/check-bgp-routes"
                },
                {
                    "instance-id" : "bgp-instance-1",
                    "playbook" : "bgp-using-openconfig",
                    "rule" : "bgp/check-bgp-state-using-openconfig"
                },
                {
                    "instance-id" : "inventory-instance-1",
                    "playbook" : "inventory",
                    "rule" : "inventory/check-system-info"
                },
                {
                    "instance-id" : "interfaces-instance-1",
                    "playbook" : "interfaces-using-openconfig",
                    "rule" : "interfaces/check-interfaces-description"
                },
                {
                    "instance-id" : "interfaces-instance-1",
                    "playbook" : "interfaces-using-openconfig",
                    "rule" : "interfaces/check-interfaces-status-using-openconfig"
                }
                ]
            }"""

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
            "instance-id" : "bgp-instance-1",
            "playbook" : "bgp-using-openconfig",
            "rule" : "bgp/check-bgp-routes",
            "variable-value" : [
            {
                "name" : "max-received",
                "value" : "130"
            }
            ]
        },
        {
            "instance-id" : "inventory-instance-1",
            "playbook" : "inventory",
            "rule" : "inventory/check-system-info",
            "variable-value" : [
            {
                "name" : "hardware-value",
                "value" : "vmx"
            },
            {
                "name" : "os-value",
                "value" : "18.2R1.9"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-status-using-openconfig",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2|ge-0/0/3"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-description",
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
            "instance-id" : "bgp-instance-1",
            "playbook" : "bgp-using-openconfig",
            "rule" : "bgp/check-bgp-routes",
            "variable-value" : [
            {
                "name" : "max-received",
                "value" : "130"
            }
            ]
        },
        {
            "instance-id" : "inventory-instance-1",
            "playbook" : "inventory",
            "rule" : "inventory/check-system-info",
            "variable-value" : [
            {
                "name" : "hardware-value",
                "value" : "vmx"
            },
            {
                "name" : "os-value",
                "value" : "18.2R1.9"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-status-using-openconfig",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2|ge-0/0/3"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-description",
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
            "instance-id" : "bgp-instance-1",
            "playbook" : "bgp-using-openconfig",
            "rule" : "bgp/check-bgp-routes",
            "variable-value" : [
            {
                "name" : "max-received",
                "value" : "130"
            }
            ]
        },
        {
            "instance-id" : "inventory-instance-1",
            "playbook" : "inventory",
            "rule" : "inventory/check-system-info",
            "variable-value" : [
            {
                "name" : "hardware-value",
                "value" : "vmx"
            },
            {
                "name" : "os-value",
                "value" : "18.2R1.9"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-status-using-openconfig",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2|ge-0/0/3"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-description",
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
            "instance-id" : "bgp-instance-1",
            "playbook" : "bgp-using-openconfig",
            "rule" : "bgp/check-bgp-routes",
            "variable-value" : [
            {
                "name" : "max-received",
                "value" : "130"
            }
            ]
        },
        {
            "instance-id" : "inventory-instance-1",
            "playbook" : "inventory",
            "rule" : "inventory/check-system-info",
            "variable-value" : [
            {
                "name" : "hardware-value",
                "value" : "vmx"
            },
            {
                "name" : "os-value",
                "value" : "18.2R1.9"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-status-using-openconfig",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-description",
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
            "instance-id" : "bgp-instance-1",
            "playbook" : "bgp-using-openconfig",
            "rule" : "bgp/check-bgp-routes",
            "variable-value" : [
            {
                "name" : "max-received",
                "value" : "130"
            }
            ]
        },
        {
            "instance-id" : "inventory-instance-1",
            "playbook" : "inventory",
            "rule" : "inventory/check-system-info",
            "variable-value" : [
            {
                "name" : "hardware-value",
                "value" : "vmx"
            },
            {
                "name" : "os-value",
                "value" : "18.2R1.9"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-status-using-openconfig",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-description",
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
            "instance-id" : "bgp-instance-1",
            "playbook" : "bgp-using-openconfig",
            "rule" : "bgp/check-bgp-routes",
            "variable-value" : [
            {
                "name" : "max-received",
                "value" : "130"
            }
            ]
        },
        {
            "instance-id" : "inventory-instance-1",
            "playbook" : "inventory",
            "rule" : "inventory/check-system-info",
            "variable-value" : [
            {
                "name" : "hardware-value",
                "value" : "vmx"
            },
            {
                "name" : "os-value",
                "value" : "18.2R1.9"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-status-using-openconfig",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-description",
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
            "instance-id" : "bgp-instance-1",
            "playbook" : "bgp-using-openconfig",
            "rule" : "bgp/check-bgp-routes",
            "variable-value" : [
            {
                "name" : "max-received",
                "value" : "130"
            }
            ]
        },
        {
            "instance-id" : "inventory-instance-1",
            "playbook" : "inventory",
            "rule" : "inventory/check-system-info",
            "variable-value" : [
            {
                "name" : "hardware-value",
                "value" : "vmx"
            },
            {
                "name" : "os-value",
                "value" : "18.2R1.9"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-status-using-openconfig",
            "variable-value" : [
            {
                "name" : "interface_name",
                "value" : "ge-0/0/0|ge-0/0/1|ge-0/0/2"
            }
            ]
        },
        {
            "instance-id" : "interfaces-instance-1",
            "playbook" : "interfaces-using-openconfig",
            "rule" : "interfaces/check-interfaces-description",
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


# update this section with your healthbot ip address
server = "100.123.35.0"
authuser = "jcluser"
authpwd = "Juniper!1"
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

# update this section with your devices details

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

tables_and_views = ["system-information.yml"]

rules = ["check-system-info.rule", "check-bgp-state-using-openconfig.rule", "check-bgp-routes.rule", "check-interfaces-status-using-openconfig.rule", "check-interfaces-description.rule"]

playbooks = ["bgp-using-openconfig.playbook", "inventory.playbook", "interfaces-using-openconfig.playbook"]

for item in tables_and_views: 
    add_tables_and_views (item)

for item in rules: 
    add_rule(item)

for item in playbooks: 
    add_playbook(item)

my_devices=yaml.load(devices)
for item in my_devices:
    add_device(item)

my_group=yaml.load(device_group)
add_device_group(my_group)

commit()

