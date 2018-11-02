from jinja2 import Template
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

def enable_interface(int):
    my_template = Template('delete interfaces {{ interface }} disable')
    device=Device(host='10.49.102.160', user='root', password='Embe1mpls')
    device.open()
    cfg=Config(device)
    cfg.load(my_template.render(interface = int), format='set')
    cfg.commit()
    device.close()

# enable_interface('10.49.102.160', 'ge-0/0/5')


