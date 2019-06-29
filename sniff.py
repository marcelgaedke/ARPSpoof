import scapy.all as scapy

interface = "wlp2s0"
scapy.sniff(iface=interface, prn=lambda x:x.summary())