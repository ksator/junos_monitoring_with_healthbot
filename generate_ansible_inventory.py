#############################################
# usage:
# vi ansible_input.yml
# python ./generate_ansible_inventory.py
#############################################

import yaml
from jinja2 import Template

def import_variables_from_file():
    my_variables_file=open('ansible_input.yml', 'r')
    my_variables_in_string=my_variables_file.read()
    my_variables_in_string=my_variables_in_string.replace('device-id', 'device_id')
    my_variables_in_yaml=yaml.load(my_variables_in_string)
    my_variables_file.close()
    return my_variables_in_yaml

def generate_ansible_inventory():
    f=open('templates/inventory.j2')
    my_template = Template(f.read())
    f.close()
    f=open('hosts','w')
    f.write(my_template.render(my_variables_in_yaml))
    f.close()
    return('done')

my_variables_in_yaml=import_variables_from_file()

generate_ansible_inventory()

