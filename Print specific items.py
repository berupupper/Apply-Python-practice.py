#open a file，looking for specific line and print specific words in the lines

a = input("Enter file name: ")
a = open(a)
count = 0
for b in a:
	b= b.rstrip()
	if not b.startswith('From '): continue
        count = count+1
	c = b.split()
	print(c[1])

for b in a: #second method
	if b.startswith('From '):
		c = b.split()
		print(c[1])
