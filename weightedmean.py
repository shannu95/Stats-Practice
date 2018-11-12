

def weightedmean(arr, weights):
	z = 0
	for x,y in zip(arr, weights):
		z+=(x*y)
		wmean = z / sum(weights)
	return wmean

n = int(input("enter the number of digits: "))
print("enter "+str(n)+" digits:")
arr = list(map(float, input().split()[:n]))
print(arr)
print("enter "+str(n)+" weights:")
weights = list(map(float, input().split()[:n]))
print(weights)
print(round(weightedmean(arr, weights),1))