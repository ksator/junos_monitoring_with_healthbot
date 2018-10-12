###################################################
# Workflow: create devices, create topics, create rules, create playbooks, create notitications, create device-groups
###################################################

###################################################
# requirements: pip install requests
###################################################

###################################################
# usage: 
# vi variables.yml
# python ./configure_healthbot.py
###################################################

###################################################
# This block indicates the various imports
###################################################

import os
import json
import yaml
import requests
from jinja2 import Template
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

##################################################
# This block defines the functions we will use
###################################################

def import_variables_from_file():
    my_variables_file=open('variables.yml', 'r')
    my_variables_in_string=my_variables_file.read()
    my_variables_in_yaml=yaml.load(my_variables_in_string)
    my_variables_file.close()
    return my_variables_in_yaml

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_healthbot_configuration_for_new_device():
    f=open('devices.j2')
    my_template = Template(f.read())
    f.close()
    for dev in my_variables_in_yaml['devices_list']: 
        f=open('devices/device_' + dev["name"],'w')
        f.write(my_template.render(dev))
        f.close()
        print 'generated healthbot configuration for device_' + dev["name"]
    return('done')

def add_device(dev):
    r = requests.post(url + '/device/' + dev["name"] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded the healthbot configuration for device_' + dev["name"]
    return r.status_code

def get_devices_name_in_running_configuration():
    r = requests.get(url + '/device/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the list of devices in the running configuration"
    pprint(r.json())
    return r.status_code

def get_devices_details_in_running_configuration():
    r = requests.get(url + '/devices/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the devices details in the running configuration "
    pprint (r.json())
    return r.status_code

def get_devices_name_in_candidate_configuration():
    r = requests.get(url + '/device/?working=true', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the list of devices in the candidate configuration"
    pprint(r.json())
    return r.status_code

def get_devices_details_in_candidate_configuration():
    r = requests.get(url + '/devices/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the devices details in the candidate configuration "
    pprint (r.json())
    return r.status_code

def commit():
    r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print 'healthbot configuration commited'
    return r.status_code


######################################################
# Below blocks are REST calls to configure healthbot
######################################################

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
my_variables_in_yaml=import_variables_from_file()
server = my_variables_in_yaml['server']
authuser = my_variables_in_yaml['authuser']
authpwd = my_variables_in_yaml['authpwd']
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

######################################################
# This block is to add devices to helathbot
######################################################

get_devices_name_in_running_configuration()

print "adding devices to healthbot"

create_directory("devices")

generate_healthbot_configuration_for_new_device()

for dev in my_variables_in_yaml['devices_list']:
    payload_file = open('devices/device_' + dev["name"], 'r')
    payload = payload_file.read()
    payload_file.close()
    add_device(dev)

get_devices_name_in_candidate_configuration()

commit()

get_devices_name_in_running_configuration()

#get_devices_details_in_running_configuration()


