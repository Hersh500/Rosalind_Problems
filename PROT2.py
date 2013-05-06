
g = open('table.txt', 'r') 
f = g.readlines() 
for i in range(0, len(f)):
	f[i] = f[i].split() 
g = open('rosalind_prot.txt', 'r')
s = g.read() 

def translate(s):
	x = []
	a = " "
	while True:
		i = 0
		x = s[i:i+3]
		for i in range(0, len(f)):
			if x in f[i]:
				a = a + f[i][0]
		if i >= (len(f)-3):
			break
		i = i + 1  
	return(a) 

print(translate(s))	 
