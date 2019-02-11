# This script loads a new configuration file on a Junos device every 60 secondes, regardless the commit time

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jinja2 import Template
from time import time, sleep

def update_junos():
    # template
    f=open('machine_learning/update_routes.j2')
    my_template = Template(f.read())
    f.close()
    # render template
    f=open('machine_learning/update_routes.conf','w')
    f.write(my_template.render())
    f.close()
    # Configure Junos device
    device=Device (host='100.123.1.0', user='jcluser', password='Juniper!1')
    device.open()
    cfg=Config(device, mode='private')
    cfg.load(path='machine_learning/update_routes.conf', format='text')
    cfg.commit()
    device.close()


starttime=time()
while True:
  update_junos()
  sleep(60 - ((time() - starttime) % 60))

