from jinja2 import Template
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

def enable_interface():
    f=open('functions/enable_interface.j2')
    my_template = Template(f.read())
    f.close()
    device=Device(host='10.49.102.160', user='root', password='Embe1mpls')
    device.open()
    cfg=Config(device)
    cfg.load('delete interfaces ge-0/0/0 disable', format='set')
    cfg.commit()
    device.close()

