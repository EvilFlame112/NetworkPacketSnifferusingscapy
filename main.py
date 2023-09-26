import socket
import struct

# Create a socket to listen for incoming packets
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
# 0x0003 is for Ethernet packets

while True:
    try:
        # Receive a packet and its header
        packet, _ = sock.recvfrom(65535)

        # Parse the Ethernet frame header (14 bytes)
        eth_header = packet[:14]
        eth_header = struct.unpack('!6s6sH', eth_header)
        dest_mac = eth_header[0].hex(':')
        src_mac = eth_header[1].hex(':')
        eth_type = hex(eth_header[2])

        # Display Ethernet header information
        print(f"Source MAC: {src_mac}, Destination MAC: {dest_mac},")
        print(f"Ethernet Type: {eth_type}")

        # Extract and display the data payload (the rest of the packet)
        data = packet[14:]
        print(f"Data Payload: {data.hex(':')}")

    except KeyboardInterrupt:
        break

sock.close()
