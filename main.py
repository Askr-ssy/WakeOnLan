#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
import sys
import socket
import binascii

# magi_packet = binascii.hexlify("FF"*6,str(mac)*16)
# row = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htonl(0x1234))
# row.bind(("wlp3s0",0))

def format_packet(mac):
    def to_hex_int(s):
        return int(s.upper(), 16)
    chars = "0123456789QWERTYUIOPASDFGHJKLZXCVBNM:-"
    mac = mac.upper()
    _ = 0
    __ = 0
    for ch in mac:
        if ch not in chars:
            print("mac error")
            sys.exit()
        if ch ==":":
            _ +=1
        elif ch == "-":
            __ +=1
    if _==5 and __==0:
        mac = mac.split(":",5)
    elif __==5 and _==0:
        mac = mac.split("-",5)

    return chr(255)*6 + "".join([chr(int(ch,16)) for ch in mac]*16) + chr(0) *6

def send_packet(packet):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    s.sendto(packet.encode(),('255.255.255.255'.encode(),9))


if __name__ == "__main__":
    if len(sys.argv)<2:
        print("usage: %s <MAC Address to wakeup>" % sys.argv[0])
        sys.exit()
    send_packet(format_packet(sys.argv[1]))
    # wake on lan 04:D4:C4:F0:71:38
    # wake on lan 9C:B6:54:A9:A3:11
