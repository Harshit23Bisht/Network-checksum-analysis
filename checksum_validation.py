from scapy.all import *

packets = rdpcap("checksum.pcapng")

for i, pkt in enumerate(packets):

    print(f"\nPacket {i+1}")

    if IP in pkt:
        ip_layer = pkt[IP]

        original_checksum = ip_layer.chksum

        del ip_layer.chksum
        new_ip = IP(bytes(ip_layer))
        calculated_checksum = new_ip.chksum

        print("IP Checksum:")
        print("Original:", hex(original_checksum))
        print("Calculated:", hex(calculated_checksum))

        if original_checksum == calculated_checksum:
            print("IP Checksum Valid")
        else:
            print("IP Checksum Invalid")


    if TCP in pkt:
        tcp_layer = pkt[TCP]

        original_checksum = tcp_layer.chksum

        del tcp_layer.chksum
        new_tcp = TCP(bytes(tcp_layer))
        calculated_checksum = new_tcp.chksum

        print("TCP Checksum:")
        print("Original:", hex(original_checksum))
        print("Calculated:", hex(calculated_checksum))

        if original_checksum == calculated_checksum:
            print("TCP Checksum Valid")
        else:
            print("TCP Checksum Invalid")


    if UDP in pkt:
        udp_layer = pkt[UDP]

        original_checksum = udp_layer.chksum

        del udp_layer.chksum
        new_udp = UDP(bytes(udp_layer))
        calculated_checksum = new_udp.chksum

        print("UDP Checksum:")
        print("Original:", hex(original_checksum))
        print("Calculated:", hex(calculated_checksum))

        if original_checksum == calculated_checksum:
            print("UDP Checksum Valid")
        else:
            print("UDP Checksum Invalid")


    if ICMP in pkt:
        icmp_layer = pkt[ICMP]

        original_checksum = icmp_layer.chksum

        del icmp_layer.chksum
        new_icmp = ICMP(bytes(icmp_layer))
        calculated_checksum = new_icmp.chksum

        print("ICMP Checksum:")
        print("Original:", hex(original_checksum))
        print("Calculated:", hex(calculated_checksum))

        if original_checksum == calculated_checksum:
            print("ICMP Checksum Valid")
        else:
            print("ICMP Checksum Invalid")
