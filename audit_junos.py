from lxml import etree
from yaml import load
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

f=open('inventory.yml', 'r')
devices_list = load(f.read())['devices_list']
f.close()

for dev in devices_list:
    print dev['device-id']
    device=Device (host=dev['host'], user=dev['authentication']['password']['username'], password=dev['authentication']['password']['password'])
    device.open()
    result=device.rpc.get_bgp_neighbor_information(normalize=True)
#    etree.dump(result)
#    result.xpath('count(//bgp-peer)')
    bgp_neighbors_list = result.findall('bgp-peer')
#    len (bgp_neighbors_list)
    for neighbor in bgp_neighbors_list:
        state = neighbor.findtext('peer-state')
        address = neighbor.findtext('peer-address')
        print 'bgp session with peer ' + address + ' is ' + state

