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
            self.addHost('h%s' %(i+1))
        for i in range(9):
            self.addSwitch('s%s' %(i+1))
        # add bidirectional links in topo0.png
        # between hosts & switches
        self.addLink('h1', 's1', bw = 10, delay='50us', loss = 12)
        self.addLink('h2', 's2', bw = 5, delay = '2ms', loss = 3)
        self.addLink('h3', 's3', bw = 7, delay = '63us', loss = 9)
        self.addLink('h4', 's4', bw = 12, delay = '40us', loss = 14)
        self.addLink('h5', 's5', bw = 15, delay = '30us', loss = 18)
        self.addLink('h6', 's6', bw = 3, delay = '5ms', loss = 2)
        # between switches
        self.addLink('s1', 's7', bw = 23, delay = '1ms', loss = 8)
        self.addLink('s2', 's7', bw = 18, delay = '2ms', loss = 9)
        self.addLink('s3', 's7', bw = 15, delay = '3ms', loss = 5)
        self.addLink('h4', 's8', bw = 19, delay = '80us', loss = 7)
        self.addLink('s5', 's8', bw = 30, delay = '95us', loss = 2)
        self.addLink('s6', 's8', bw = 20, delay = '60us', loss = 6)
        self.addLink('s7', 's9', bw = 40, delay = '5ms', loss = 2)
        self.addLink('s8', 's9', bw = 50, delay = '4ms', loss = 3)

def task():
    # Create a topology
    topo = Topo0()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(topo = topo, controller = OVSController, link = TCLink)
    # Start a network
    net.start()
    # Dump every hosts and switches connections
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
    # Enter the CLI mode
    CLI(net)

if __name__ == '__main__':
    task()
