# network_scanning.py
from scapy.all import ARP, Ether, srp

def scan_network(network):
    print("Starting network scan...")
    # Ethernet çerçevesi ve ARP isteği paketi oluşturma
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=network)
    packet = ether / arp
    
    # Paketi gönder ve yanıtları al
    responses, _ = srp(packet, timeout=2, verbose=False)
    
    # Bulunan IP adreslerini sakla
    ip_list = []
    for response in responses:
        ip_list.append(response[1].psrc)
    
    return ip_list
