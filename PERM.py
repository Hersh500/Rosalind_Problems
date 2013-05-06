import itertools
import math
n=int(input("Enter n"))
def perms(n):
	nums = []
	perms = []
	for i in range(1, n+1):
		nums.append(i)
	return nums 
print (math.factorial(n))
nums = perms(n)
lst = list(itertools.permutations(nums))
#print (lst)
for item in lst: 
	x = str(item).replace(',','')
	x = x.replace('(', '')
	print(x.replace(')', ''))
