from yaml import load
from jnpr.junos.utils.sw import SW
from jnpr.junos import Device

f=open('inventory.yml', 'r')
devices_list = load(f.read())['devices_list']
f.close()

pkgs_list = ['network-agent-x86-32-18.2R1-S3.2-C1.tgz', 'junos-openconfig-x86-32-0.0.0.10-1.tgz']

for pkg in pkgs_list:
    for item in devices_list:
        print 'adding the package ' + pkg + ' to the device ' + item['device-id']
        device=Device (host=item['host'], user=item['authentication']['password']['username'], password=item['authentication']['password']['password'])
        device.open()
        sw = SW(device)
        sw.install(package=pkg, validate=False, no_copy=False, progress=True, remote_path="/var/home/jcluser")
        device.close()


