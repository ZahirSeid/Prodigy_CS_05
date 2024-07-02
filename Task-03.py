import scapy.all as scapy

def sniff_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        payload = packet[scapy.Raw].load if packet.haslayer(scapy.Raw) else None

        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol}")
        if payload:
            print("Payload:", payload.hex())

def main():
    interface = input("Enter the interface to sniff packets (e.g., eth0): ")
    sniff_packets(interface)

if __name__ == "__main__":
    main()
