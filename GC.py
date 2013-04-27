dct = {}
gc_contents = []
def getfile():
	g = input("enter the filename")
	f = open(g, 'r')
	lst = []
	i = -1
	for line in f.readlines():
		if ">" in line:
			i = i + 1 
			lst.append([line])
		else:
			lst[i].append(line)
	for i in range(0, len(lst)):
		for j in range(0, len(lst[i])):
			lst[i][j] = lst[i][j].rstrip("\n")
	return (lst) 	
def read(s):
	gc = 0
	length = 0 
	for i in range(1, len(s)):
		gc = gc + s[i].count("G") + s[i].count("C")
		length = length + len(s[i]) 
	gc = gc/(length) * 100 
	dct[gc] = s[0] 
	gc_contents.append(gc)
lst = getfile()
for i in range(0, len(lst)):
	read(lst[i]) 
mx = 0 
for item in gc_contents:
	if item > mx:
		mx = item 
print (dct[mx])
print (mx) 		


