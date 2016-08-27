#! /usr/bin/python

import sys
import socket
import telnetlib
import re

def f(x):
        return ((x * (x + 1)) / 2)
def fib(n):
        a = 0
        b = 1
        for i in range(1 , n):
                a, b = b, a + b

        return b



'''
def fib(n):
        a = 0
        b = 1
        for i in range (0, n):
                n = fib(n - 1) + fib(n - 2)
        return n

'''

try:
        s = socket.create_connection(("128.199.236.209", 17845))
except socket.gaierror as e:
        (n, q) = e

        print "Error: " + q + ", Errno: " + str(n)

        sys.exit(-1)

buf = s.recv(8192)
buf = s.recv(8192)

r = re.findall(r"(.*)(\:)(\x20)(\d+)", buf.rstrip(chr(0x0a)))

q = str(f(int(r[0][3])))
q += chr(0x0a)

print q.rstrip(chr(0x0a))

s.send(q)

for i in range(0, 8):
        buf = s.recv(8192)

        r = re.findall(r"(.*)(\:)(\x20)(\d+)", buf.rstrip(chr(0x0a)))

        q = str(f(int(r[0][3])))
        q += chr(0x0a)

        print q.rstrip(chr(0x0a))

        s.send(q)

buf = s.recv(8192)
buf = s.recv(8192)


f_tuple = []

print buf

r = re.findall(r"(.*)(\:)(\x20)(\d+)", buf.rstrip(chr(0x0a)))

q = int(r[0][3])


for i in range(0, (q + 1)):
        f_tuple.append(fib(i))

s.send(str(f_tuple[q]) + chr(0x0a))

print f_tuple[q]

'''
while True:
        buf = s.recv(8192)

        print buf

        r = re.findall(r"(.*)(\:)(\x20)(\d+)", buf.rstrip(chr(0x0a)))

        q = str(fib(int(r[0][3])))
        q += chr(0x0a)

        print q

        s.send(q)
'''

t = telnetlib.Telnet()
t.sock = s
t.interact()