import json
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

server = '100.123.35.0'
authuser = "jcluser"
authpwd = "Juniper!1"
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

network_group = """{
                "network-group-name" : "BGP",
                "description" : "zoom for BGP troubleshooting",
                "playbooks" : ["bgp-zoom"],
                "variable" : [
                {
                    "instance-id" : "vmx1-vmx4",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
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
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
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
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
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
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
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
                    "instance-id" : "vmx1-vmx6",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
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
                        "value" : "192.168.1.5"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.1.4"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx1-vmx6",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
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
                        "value" : "192.168.1.5"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.1.4"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx1-vmx7",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
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
                        "value" : "192.168.1.7"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.1.6"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx1-vmx7",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
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
                        "value" : "192.168.1.7"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.1.6"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx2-vmx4",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.2.1"
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
                        "value" : "192.168.2.0"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx2-vmx4",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.2.1"
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
                        "value" : "192.168.2.0"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx2-vmx5",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.2.3"
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
                        "value" : "192.168.2.2"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx2-vmx5",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.2.3"
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
                        "value" : "192.168.2.2"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx2-vmx6",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.2.5"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.2.4"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx2-vmx6",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.2.5"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.2.4"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx2-vmx7",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.2.7"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.2.6"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx2-vmx7",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX2"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.2.7"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.2.6"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx3-vmx4",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.3.1"
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
                        "value" : "192.168.3.0"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx3-vmx4",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.3.1"
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
                        "value" : "192.168.3.0"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx3-vmx5",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.3.3"
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
                        "value" : "192.168.3.2"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx3-vmx5",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.3.3"
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
                        "value" : "192.168.3.2"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx3-vmx6",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.3.5"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.3.4"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx3-vmx6",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.3.5"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX6"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.3.4"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx3-vmx7",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-peer-type",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.3.7"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.3.6"
                    }
                    ]
                },
                {
                    "instance-id" : "vmx3-vmx7",
                    "playbook" : "bgp-zoom",
                    "rule" : "bgp/troubleshooting-as",
                    "variable-value" : [
                    {
                        "name" : "device1-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device1-name-variable",
                        "value" : "vMX3"
                    },
                    {
                        "name" : "device1-peer-variable",
                        "value" : "192.168.3.7"
                    },
                    {
                        "name" : "device2-group-variable",
                        "value" : "vmx"
                    },
                    {
                        "name" : "device2-name-variable",
                        "value" : "vMX7"
                    },
                    {
                        "name" : "device2-peer-variable",
                        "value" : "192.168.3.6"
                    }
                    ]
                }
                ]
            }"""



def troubleshoot_bgp(**kwargs):
   requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
   my_network_group=yaml.load(network_group)
   payload=json.dumps(my_network_group)
   r = requests.post(url + '/network-group/' + my_network_group['network-group-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
   print ('loaded healthbot configuration for the network group: ' + my_network_group['network-group-name'])
   r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
   print ('healthbot configuration commited!')


