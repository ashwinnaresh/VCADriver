import os
#import time
#import sys
#import novaclient.v1_1.client as nvclient
#from credentials import get_nova_creds
from vcloudair import VCloudDriver
def federate(n,f):
        #creds = get_nova_creds()
        vca = VCloudDriver()
        name = n
        #image = nova.images.find(name=i)
        flavor = f#nova.flavors.find(ram=f)
        instance = nova.servers.create(name=name, image=image, flavor=flavor)

        # Poll at 5 second intervals, until the status is no longer 'BUILD'
        status = instance.status
        while status == 'BUILD':
                time.sleep(5)
                # Retrieve the instance again so the status field updates
                instance = nova.servers.get(instance.id)
                status = instance.status
#print "status: %s" % status
#floating_ip = nova.floating_ips.create()
#instance.add_floating_ip(floating_ip)
