#!/usr/bin/python

# import modules from mininet python api
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.cli import CLI

# Create a topo class according to topo0.png
class Topo0(Topo):
    def build(self):
        # add 6 hosts & 9 switches
        for i in range(6):
            host = self.addHost('h%s' %(i+1))
        for i in range(9)
            switch = self.addSwitch('s%s' %(i+1))

def task():
    # Create a topology
    topo = Topo0()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(topo = topo, controller = OVSController, link = TCLink)
    # Start a network
    net.start()
    # Dump every hosts’ and switches’ connections
    dumpNodeConnections(net.hosts);
    # Enter the CLI mode
    CLI(net)

if __name__ == '__main__':
    task()