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
server = "100.123.35.0"
authuser = "jcluser"
authpwd = "Juniper!1"
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

# update this section with your devices details

# update this section with your device group details

network_group = """{
                "network-group-name" : "BGP",
                "description" : "BGP troubleshooting",
                "playbooks" : ["bgp-troubleshooting"],
                "variable" : [
                {
                    "instance-id" : "vmx1-vmx4",
                    "playbook" : "bgp-troubleshooting",
                    "rule" : "bgp/compare-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX1"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.1.1"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX4"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.1.0"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx1-vmx4",
                    "playbook" : "bgp-troubleshooting",
                    "rule" : "bgp/compare-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX1"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.1.1"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX4"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.1.0"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx1-vmx5",
                    "playbook" : "bgp-troubleshooting",
                    "rule" : "bgp/compare-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX1"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.1.3"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX5"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.1.2"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx1-vmx5",
                    "playbook" : "bgp-troubleshooting",
                    "rule" : "bgp/compare-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX1"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.1.3"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX5"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.1.2"
                    }
                    ]
                }
                ]
            }"""

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

rules = ["compare-as.rule", "compare-peer-type.rule"]

for item in rules:
    add_rule(item)

add_playbook("bgp-troubleshooting.playbook")

my_network_group=yaml.load(network_group)
add_network_group(my_network_group)

commit()


