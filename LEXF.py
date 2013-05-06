from itertools import product
def perm(s,n):
	return (list(product(s, repeat=n)))
g = open('rosalind_lexf (1).txt','r')
f = (g.readline()).split() 
n = g.readline()
lst = perm(f,int(n))
for item in lst: 
	x = str(item).replace('(','')
	x = x.replace(',', '')
	x = x.replace(' ','')
	x = x.replace("'",'')
	print(x.replace(')', ''))
