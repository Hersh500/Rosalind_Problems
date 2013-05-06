def getfile():
	g = open('mass.txt', 'r')
	return(g.readlines())
def calc(s,f):
	sm = 0 
#	print (f)
	for item in s:
		for i in range(0, len(f)):
			if item in f[i]:
				sm = sm + float(f[i][1])
	return (sm)
s = open('rosalind_prtm.txt', 'r').read() 
f = getfile()
for i in range(0, len(f)):
	f[i] = f[i].split()
print(calc(s,f))
