#############################################
# usage:
# vi variables.yml
# python ./generate_vars_for_ansible.py
#############################################

import os
import yaml
from jinja2 import Template

def import_variables_from_file():
    my_variables_file=open('variables.yml', 'r')
    my_variables_in_string=my_variables_file.read()
    my_variables_in_string=my_variables_in_string.replace('device-id', 'device_id')
    my_variables_in_string=my_variables_in_string.replace('open-config', 'open_config')
    my_variables_in_string=my_variables_in_string.replace('system-id', 'system_id')
    my_variables_in_yaml=yaml.load(my_variables_in_string)
    my_variables_file.close()
    return my_variables_in_yaml

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_junos_vars_for_ansible():
    f=open('templates/devices_yml.j2')
    my_template = Template(f.read())
    f.close()
    for dev in my_variables_in_yaml['devices_list']:
        f=open('host_vars/' + dev["device_id"] + '/generated_vars.yml','w')
        f.write(my_template.render(dev))
        f.close()
    return('done')

def generate_healthbot_vars_for_ansible():
    f=open('templates/healthbot_server_yml.j2')
    my_template = Template(f.read())
    f.close()
    f=open('host_vars/healthbot_server/generated_vars.yml','w')
    f.write(my_template.render(ansible_host = my_variables_in_yaml['server'], authuser = my_variables_in_yaml['authuser'], authpwd = my_variables_in_yaml['authpwd']))
    f.close()
    return('done')

my_variables_in_yaml=import_variables_from_file()

for item in ["host_vars", "host_vars/healthbot_server"]:
    create_directory(item)

for dev in my_variables_in_yaml['devices_list']:
    create_directory("host_vars/" + dev["device_id"])

generate_junos_vars_for_ansible()

generate_healthbot_vars_for_ansible()
