import os
import yaml
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def import_variables_from_file():
    my_variables_file=open('variables.yml', 'r')
    my_variables_in_string=my_variables_file.read()
    my_variables_in_yaml=yaml.load(my_variables_in_string)
    my_variables_file.close()
    return my_variables_in_yaml

def add_tables_and_views(file_name):
    files = {'up_file': open('tables_and_views/' + file_name,'r')}
    r=requests.post(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print "added table: " + file_name 
    return r.status_code

def add_rule(file_name):
    files = {'up_file': open('rules/' + file_name,'r')}
    r=requests.post(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print "added table: " + file_name 
    return r.status_code

def add_playbook(file_name):
    files = {'up_file': open('playbooks/' + file_name,'r')}
    r=requests.post(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json' }, verify=False, files=files)
    print "added table: " + file_name 
    return r.status_code

def get_file(file_name):
    print table
    r=requests.get(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers={ 'Accept' : 'application/json', 'Content-Type': 'multipart/form-data' }, verify=False)
    print r.content
    return r.status_code

def delete_file(file_name):
    print "removing file: " + file_name
    r = requests.delete(url + '/files/helper-files/' + file_name, auth=HTTPBasicAuth(authuser, authpwd), headers=headers, verify=False)
    return r.status_code

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

my_variables_in_yaml=import_variables_from_file()
server = my_variables_in_yaml['server']
authuser = my_variables_in_yaml['authuser']
authpwd = my_variables_in_yaml['authpwd']
url = 'https://'+ server + ':8080/api/v1'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }

rules_list=os.listdir('rules')
playbooks_list=os.listdir('rules')
tables_and_views_list=os.listdir('tables_and_views')

for table in tables_and_views_list: 
    add_tables_and_views(table)

for rule in rules_list:
    add_rule(rule)

for playbook in playbooks_list: 
    add_playbook(playbook)

for table in tables_and_views_list: 
    get_file(table)

for rule in rules_list:
    get_file(rule)

for playbook in playbooks_list: 
    get_file(playbook)    

for playbook in playbooks_list: 
    delete_file(playbook)

for rule in rules_list:
    delete_file(rule)

for table in tables_and_views_list: 
    delete_file(table)



