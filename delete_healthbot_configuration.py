###################################################
# About this scrit:
# delete your own tables, topics, rules, playbooks, groups, notifications, devices
# commit the change and display new running configuration
###################################################

###################################################
# requirements: pip install requests
###################################################

###################################################
# usage:
# vi variables.yml
# python ./delete_healthbot_configuration
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

def get_devices_name_in_running_configuration():
    r = requests.get(url + '/device/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the list of devices in the running configuration"
    pprint(r.json())
    return r.json()

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

def delete_device(dev):
    r = requests.delete(url + '/device/' + dev + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    return r.status_code

def get_device_groups():
    r = requests.get(url + '/device-group/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the list of device groups in the running configuration"
    pprint (r.json())
    return (r.json())

def delete_device_group(group):
    r = requests.delete(url + '/device-group/'+ group + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    return r.status_code

def update_device_group(group):
    if 'playbooks' in group:
        del group['playbooks']
    if 'variable' in group:
        del group['variable']
    payload=json.dumps(group)
    r = requests.post(url + '/device-group/' + group['device-group-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False, data=payload)
    return r.status_code

def get_notifications():
    r = requests.get(url + '/notification/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the notifications in the ruuning configuration "
    pprint (r.json())
    return (r.json())

def delete_notification(notification):
    r = requests.delete(url + '/notification/' + notification + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    return r.status_code

def delete_table(table):
    r = requests.delete(url + '/files/helper-files/' + table, auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    return r.status_code

def delete_playbook(playbook):
    r = requests.delete(url + '/playbook/' + playbook['playbook-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    return r.status_code

def get_playbook(playbook):
    r = requests.get(url + '/playbook/' + playbook['playbook-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the playbook " + playbook["playbook-name"] + " details in the running configuration"
    pprint (r.json())
    return (r.json())

def delete_rule(topic, rule):
    r = requests.delete(url + '/topic/' + topic + '/rule/' + rule['rule-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    return r.status_code

def delete_topic(topic):
    r = requests.delete(url + '/topic/' + topic['topic-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    return r.status_code

def get_topics():
    r = requests.get(url + '/topic/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the list of topics in the running configuration"
    pprint (r.json())
    return (r.json())

def get_topic(topic):
    r = requests.get(url + '/topic/' + topic['topic-name'] + '/', auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    print "here's the topic " + topic["topic-name"] + " details in the running configuration"
    pprint (r.json())
    return (r.json())



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
# This block is to remove your own device groups from healthbot
######################################################

print '########### Removing playbook instances and variables from your own device groups  ############'

for item in my_variables_in_yaml['device_groups']:
    print "updating device group " + item['device-group-name']
    update_device_group(item)

print "commiting the change"
commit()

print '########### Removing your own device groups  ############'

for item in my_variables_in_yaml['device_groups']:
    print "removing device group " + item['device-group-name']
    delete_device_group(item['device-group-name'])


######################################################
# This block is to remove your own tables and views from healthbot
######################################################

print '########### Removing your own tables (tables and views)  ############'

for item in my_variables_in_yaml['tables_and_views']:
     print "removing table " + item
     delete_table(item)


######################################################
# This block is to remove your own playbooks from healthbot
######################################################

print '########### Removing your own playbooks  ############'

for item in my_variables_in_yaml['playbooks']:
     print "removing playbook " + item['playbook-name']
     delete_playbook(item)


######################################################
# This block is to remove your own topics and rule from healthbot
######################################################

print '########### Removing your own topics and rules ############'

for item in my_variables_in_yaml['topics']:
     print "removing topic " + item['topic-name']
     delete_topic(item)


######################################################
# This block is to remove all notifications from healthbot
######################################################

print '###########  Removing your own notifications  ############'

for item in my_variables_in_yaml['notifications']:
    print "removing notification " + item['notification-name']
    delete_notification(item['notification-name'])

######################################################
# This block is to remove your own devices from healthbot
######################################################

print '###########  Removing your own devices  ############'

for item in my_variables_in_yaml['devices_list']:
    print "removing device " + item['device-id']
    delete_device( item['device-id'])


######################################################
# This block is to commit the changes and to display the running configuration
######################################################

print '###########  committing the configuration change  ############'

commit()

print '###########  printing running configuration  ############'

for item in my_variables_in_yaml['topics']:
     get_topic(item)

for item in my_variables_in_yaml['playbooks']:
     get_playbook(item)

get_notifications()
get_device_groups()
get_devices_name_in_running_configuration()


