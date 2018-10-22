############################################################################################################################
# This script prints some details of the healthbot configuration
############################################################################################################################

############################################################################################################################
# requirements: pip install requests
############################################################################################################################

############################################################################################################################
# usage:
# vi variables.yml
# python ./audit_healthbot.py
############################################################################################################################

############################################################################################################################
# This block indicates the various imports
############################################################################################################################

import os
import json
import yaml
import requests
from jinja2 import Template
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

############################################################################################################################
# This block defines the functions we will use
############################################################################################################################

def import_variables_from_file():
    my_variables_file=open('variables.yml', 'r')
    my_variables_in_string=my_variables_file.read()
    my_variables_in_yaml=yaml.load(my_variables_in_string)
    my_variables_file.close()
    return my_variables_in_yaml

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_devices_name_in_running_configuration():
    r = requests.get(url + '/device/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** list of devices in running configuration ******************'
    pprint(r.json())
    return r.status_code

def get_device_details_in_running_configuration(device):
    r = requests.get(url + '/device/' + device['device-id'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** device '+ device['device-id'] + ' ******************'
    pprint (r.json())
    return r.status_code


def get_devices_details_in_running_configuration():
    r = requests.get(url + '/devices/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** devices details in running configuration ******************'
    pprint (r.json())
    return r.status_code

def get_devices_name_in_candidate_configuration():
    r = requests.get(url + '/device/?working=true', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** list of devices in candidate configuration ******************'
    pprint(r.json())
    return r.status_code

def get_devices_details_in_candidate_configuration():
    r = requests.get(url + '/devices/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** devices details in candidate configuration ******************'
    pprint (r.json())
    return r.status_code

def get_tables_and_views(table):
    files = {'up_file': open('tables_and_views/' + table,'r')}
    r=requests.get(url + '/files/helper-files/' + table, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json', 'Content-Type': 'multipart/form-data' }, verify=False)
    print '\n****************** table ' + table  + ' ******************'
    print r.content
    return r.status_code

def get_device_group(group):
    r = requests.get(url + '/device-group/'+ group + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** device group ' + group + ' ******************'
    pprint (r.json())
    return r.status_code

def get_device_groups():
    r = requests.get(url + '/device-group/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** list of devices groups in running configuration ******************'
    pprint (r.json())
    return r.status_code

def get_notification(notification):
    r = requests.get(url + '/notification/'+ notification['notification-name']  + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False
)
    print '\n****************** notification ' + notification['notification-name'] + ' ******************'
    pprint (r.json())
    return r.status_code

def get_notifications():
    r = requests.get(url + '/notification/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** list of notifications in running configuration ******************'
    pprint (r.json())
    return r.status_code

def get_playbooks():
    r = requests.get(url + '/playbook/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** list of playbooks in running configuration ******************'
    pprint (r.json())
    return r.status_code

def get_playbook(playbook):
    r = requests.get(url + '/playbook/'+ playbook['playbook-name']  + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False
)
    print '\n****************** playbook ' + playbook['playbook-name'] + ' ******************'
    pprint (r.json())
    return r.status_code

def get_topics():
    r = requests.get(url + '/topic/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** list of topics in running configuration ******************'
    pprint (r.json())
    return r.status_code

def get_topic(topic):
    r = requests.get(url + '/topic/'+ topic['topic-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** topic '+ topic['topic-name'] + ' ******************'
    pprint (r.json())
    return r.status_code

def get_rules(topic):
    r = requests.get(url + '/topic/' + topic + '/rule/' , auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    pprint (r.json())
    return r.status_code

def get_rule(topic, rule):
    r = requests.get(url + '/topic/' + topic + '/rule/' + rule['rule-name'] + '/' , auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print '\n****************** rule '+ topic + '/' + rule['rule-name'] + ' ******************'
    pprint (r.json())
    return r.status_code


############################################################################################################################
# Below block is the REST calls to print healthbot configuration
############################################################################################################################

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
my_variables_in_yaml=import_variables_from_file()
server = my_variables_in_yaml['server']
authuser = my_variables_in_yaml['authuser']
authpwd = my_variables_in_yaml['authpwd']
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

get_devices_name_in_running_configuration()

for item in my_variables_in_yaml['devices_list']:
    get_device_details_in_running_configuration(item)

for item in my_variables_in_yaml['tables_and_views']:
    get_tables_and_views(item)

get_notifications()

for item in my_variables_in_yaml['notifications']:
    get_notification(item)

get_topics()

for item in my_variables_in_yaml['topics']:
    get_topic(item)

for item in my_variables_in_yaml['rules']:
     get_rule('ksator.bgp', item)

get_playbooks()

for item in my_variables_in_yaml['playbooks']:
    get_playbook(item)

get_device_groups()

for item in my_variables_in_yaml['device_groups']:
    get_device_group(item['device-group-name'])


