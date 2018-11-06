from jinja2 import Template
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def get_junos_details(dev):
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	healthbot_user = 'root'
	healthbot_pwd = 'jfit'
	healthbot_server = '10.209.18.74'
	headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json' }
	url = 'https://'+ healthbot_server + ':8080/api/v1/device/' + dev +'/'
	r = requests.get(url, auth=HTTPBasicAuth(healthbot_user, healthbot_pwd), headers=headers, verify=False)
	return r.json()

def enable_interface(int):
	junos_details = get_junos_details('device_id')
	junos_host = junos_details['host']
	junos_user = junos_details['authentication']['password']['username']
	# junos_password = junos_details['authentication']['password']['password']
	junos_password = 'MaRtInI'
	device=Device(host=junos_host, user=junos_user, password=junos_password)
	device.open()
	cfg=Config(device)
	my_template = Template('delete interfaces {{ interface }} disable')
	cfg.load(my_template.render(interface = int), format='set')
	cfg.commit()
	device.close()

