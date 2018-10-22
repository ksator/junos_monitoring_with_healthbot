############################################################################################################################
# This script get the desired healthbot configuration from the file variables.yml, and configures healthbot using REST calls
# It configures devices, notifications, topics, rules, playbooks, device-groups. It adds tables (tables and views).
############################################################################################################################

############################################################################################################################ 
# requirements: pip install requests
############################################################################################################################

############################################################################################################################
# usage:
# vi variables.yml
# python ./configure_healthbot.py
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

def add_device(dev):
    payload=json.dumps(dev)
    r = requests.post(url + '/device/' + dev['device-id'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the device: ' + dev['device-id']
    return r.status_code

def add_tables_and_views(table):
    files = {'up_file': open('tables_and_views/' + table,'r')}
    r=requests.post(url + '/files/helper-files/' + table, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print "added table: " + table 
    return r.status_code

def add_device_group(group):
    payload=json.dumps(group)
    r = requests.post(url + '/device-group/' + group['device-group-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the device group: ' + group['device-group-name']
    return r.status_code

def add_notification(notification):
    payload=json.dumps(notification)
    r = requests.post(url + '/notification/' + notification['notification-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the notification: ' + notification['notification-name']
    return r.status_code

def add_playbook(playbook):
    payload=json.dumps(playbook)
    r = requests.post(url + '/playbook/' + playbook['playbook-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the playbook: ' + playbook['playbook-name']
    return r.status_code

def add_topic(topic):
    payload=json.dumps(topic)
    r = requests.post(url + '/topic/' + topic['topic-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the topic: ' + topic['topic-name']
    return r.status_code

def add_rule(topic, rule):
    payload=json.dumps(rule)
    r = requests.post(url + '/topic/' + topic + '/rule/' + rule['rule-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    print 'loaded healthbot configuration for the rule: ' + topic + '/' + rule['rule-name']
    return r.status_code

def commit():
    r = requests.post(url + '/configuration', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print 'healthbot configuration commited!'
    return r.status_code

############################################################################################################################
# Below blocks are REST calls to configure healthbot
############################################################################################################################

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
my_variables_in_yaml=import_variables_from_file()
server = my_variables_in_yaml['server']
authuser = my_variables_in_yaml['authuser']
authpwd = my_variables_in_yaml['authpwd']
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

############################################################################################################################
# This block is to add devices to healthbot
############################################################################################################################

print '****************** Adding devices to healthbot ******************'

for item in my_variables_in_yaml['devices_list']:
    add_device(item)

############################################################################################################################
# This block is to add tables (tables and views) to healthbot
############################################################################################################################

print '****************** Adding tables to healthbot ******************'

for item in my_variables_in_yaml['tables_and_views']:
    add_tables_and_views(item)

############################################################################################################################
# This block is to add notifications to healtbot
############################################################################################################################

print '****************** Adding notifications to healthbot ******************'

for item in my_variables_in_yaml['notifications']:
    add_notification(item)

############################################################################################################################
# This block is to add topics and rules to healtbot
############################################################################################################################

print '****************** Adding topics and rules to healthbot ******************'

for item in my_variables_in_yaml['topics']:
    add_topic(item)


############################################################################################################################
# This block is to add playbooks to healthbot
############################################################################################################################

print '****************** Adding playbooks to healthbot ******************'

for item in my_variables_in_yaml['playbooks']:
    add_playbook(item)

############################################################################################################################
# This block is to add device groups to healtbot
############################################################################################################################

print '****************** Adding device groups to healthbot ******************'

for item in my_variables_in_yaml['device_groups']:
    add_device_group(item)


############################################################################################################################
# This block is to commit healthbot configuration
############################################################################################################################

print '****************** commiting healthbot configuration ******************'

commit()

