import itertools
import os

try:
	os.system("figlet Dictionary")#install figlet package if needed
except:
	print("")	
minSize = int(input('[*] Minimum size of the words : '))
maxSize = int(input('[*] Maximum size of the words : '))
print("\n[1] Only alphabets\n[2] Only Numbers\n[3] Alphanumeric\n")
types = int(input('Your choice : '))

alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
alphaNumeric = alpha + num

name = input('Set the name(or path) of the wordlist to be created : ')

l = [alpha, num, alphaNumeric]


file = open(name, "w")
count = 0

for i in range(minSize,maxSize + 1):
	for xs in itertools.product(l[types-1], repeat=i):
		file.write(''.join(xs) + '\n')
		count+=1

file.close()

print("\n\033[1;32;40m[+] Wordlist generated : " + name + " - " + str(count) + " lines")
	





