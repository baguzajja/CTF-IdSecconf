from pwn import *

r = remote("128.199.236.209", 17845)

print r.recvuntil("Pola Token Segitiga...")

def tri(n):
	return n * (n + 1) / 2

def fib(n):
	a, b = 0, 1

	for _ in range(n):
		a, b = b, a + b

	return a

for i in range(9):
	print r.recvuntil("index Ke: ")

	soal = r.recvline().strip()
	print "[-] Soal:  " + soal

	jawaban = tri(int(soal))
	print "[+] Jawab: " + str(jawaban)

	r.send(str(jawaban))

print r.recvuntil("Fibonacci!:")

for i in range(9):
	print r.recvuntil("index: ")

	soal = r.recvline().strip()
	print "[-] Soal:  " + soal

	jawaban = fib(int(soal)-1)
	print "[+] Jawab: " + str(jawaban)

	r.send(str(jawaban))

print r.recv(1024)