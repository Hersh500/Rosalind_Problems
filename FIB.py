

def cycles(months, litter):
	mature_rabbits = 1
	immature_rabbits = 0 
	for i in range(1, months): 
		temp = immature_rabbits
		immature_rabbits = 0 
		immature_rabbits += (mature_rabbits * litter) 
		mature_rabbits += temp 
		print(mature_rabbits, immature_rabbits)
	return (mature_rabbits)

def get_info():
	g = open("rosalind_fib.txt", 'r')
	f = [int(c) for c in g.readline().split()]
	return (f[0], f[1])

months, litter = get_info()

print(cycles(months, litter))
