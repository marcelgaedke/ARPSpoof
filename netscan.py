import scapy.all as scapy


#scapy.ls(scapy.ARP)

arp_request = scapy.ARP(pdst="192.168.177.1/24")
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
arp_request_broadcast = broadcast/arp_request
#arp_request_broadcast.show()
answered, unanswered = scapy.srp(arp_request_broadcast,timeout=2,verbose=False)
for element in answered:
    print(element[1].summary())