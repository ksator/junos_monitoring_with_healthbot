from jinja2 import Template
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

def enable_interface(dev, int):
    f=open('functions/enable_interface.j2')
    my_template = Template(f.read())
    f.close()
    device=Device(host=dev, user='root', password='Embe1mpls')
    device.open()
    cfg=Config(device)
    cfg.load(my_template.render(interface = int), format='set')
    cfg.commit()
    device.close()

enable_interface('10.49.102.160', 'ge-0/0/5')

