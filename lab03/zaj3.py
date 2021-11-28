import bluetooth
import sys
from pprint import pprint


nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))

service = bluetooth.find_service(address = '7C:F3:1B:77:43:73')

pprint(service)