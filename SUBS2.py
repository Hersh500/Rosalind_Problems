def substr(t, s):
	positions = []
	x = len(s)
	print (len(t))
	for i in range(0, x):
		if s[i] == t[0]:
			y = True
			if i + len(t) > len(s):
				pass
			else: 
				for j in range(0, len(t)):
					if s[i+j] != t[j]:
						y = False
						break 
				if y:
					positions.append(i + 1) 
	return (positions) 
s = input("Enter s")
t = input("Enter t") 
print (substr(t, s))
