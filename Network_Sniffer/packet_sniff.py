#importing necessary libraries for the getting network packet information
import socket
import struct
import textwrap
import scapy.all as scapy
from scapy.layers import http


def main():
    print("WELCOME TO CUSTOM PACKET SNIFFING TOOL")
    print("--------------------------------------")
    n = int(input("1 - TIGHT SNIFFING, 2- LOOSE SNIFFING: "))
    if n == 1:
       interface = input("ENTER INTERFACE FOR SCANNING: ")
       sniff_tight(interface)  
    elif n == 2:
       sniff_loose()
    else:
       print("Wrong option, quitting! ")
       exit


# tight sniffing
def sniff_tight(interface):
    scapy.sniff(iface = interface, store=False, prn = process_packet)
    
# processing sniffing packets
def process_packet(packet):
    #n = int(input("3 - for all packet info, 4 - for http packet: "))
    print(packet)
    if packet.haslayer(http.HTTPRequest):
       print(packet[http.HTTPRequest].Host)
    
    
       
    #print(packet.show())
    
  
    

def sniff_loose():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    while True:
        raw_data, addr = conn.recvfrom(65535)
        dest_mac, src_mac , eth_proto, data = ethernet_frame(raw_data)
        print("\nWlan_frame:")
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))
        
        
        
#function for unpacking the interface 
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[:14]
    
#formatted MAC address i.e - AA:BB:CC:DD:EE:FF
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)#for getting the useful mac address info
    return ':'.join(bytes_str).upper() #joining by colon ":" and making all of them in upper case
   
main()
#sniff_loose()
