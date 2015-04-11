__author__ = 'xsc'
'''
This demo shows how to parse pcap files using scapy.
For more details, see http://www.secdev.org/projects/scapy/doc/
Another example is in http://thepacketgeek.com/importing-packets-from-trace-files/.
'''

from scapy.all import *

# a=rdpcap("/spare/captures/isakmp.cap")

pcap_file_name = 'IBGP_adjacency.cap'
reader = PcapReader(pcap_file_name)
for packet in reader:
    if packet.haslayer('UDP'):
        udp = packet[2]  #packet[0] is Ethernet header, packet[1] is IP header, packet[2] is TCP header
        print udp.load
