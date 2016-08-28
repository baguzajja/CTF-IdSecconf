#!/usr/bin/python2
# Author: Gandung Prakoso [ tesla_ ]

import socket, sys
sys.setrecursionlimit(10000000)

my_host = "128.199.236.209"
my_port = 17845
sock = socket.create_connection((my_host,my_port))

def kali(A, B):
	a, b, c = A
	d, e, f = B

	return a * d + b * e, a * e + b * f, b * e + c * f

def pow(A, n):
	if n == 1:
		return A
	if n & 1 == 0:
		return pow(kali(A, A), n / 2)
	else:
		return kali(A, pow(kali(A, A), (n - 1) / 2))

def fibo(n):
	a, b = 0, 1

	for _ in range(n):
		a, b = b, a + b

	return a

triangular = lambda x:x * (x + 1) / 2
data = sock.recv(1024)

while data:
	first_recv = sock.recv(1024)

	if "Kamu punya" in first_recv:
		num1 = first_recv
		print num1

		solve = triangular(int(num1[num1.index(":") + 1:]))
		sock.send(str(solve))
		print solve,num1

	if "Waktumu " in first_recv:
		fib = int(first_recv[first_recv.index(":") + 1:])
		fib = fibo(fib-1)

		print first_recv
		sock.send(str(fib))
		print fib
		#print sock.recv(1024)
	else:
		sys.stdout.write(first_recv)

#print num1
#print str(num1[54:])