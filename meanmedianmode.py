from collections import Counter
from scipy import stats

def mean(arry):
	avg = sum(arry)/len(arry)
	return avg

def median(arr):
	x = sorted(arr)
	if (len(x) % 2) == 0:
		arr = (x[int((len(x)-1)/2)], x[int((len(x)+1)/2)])
		med = sum(arr)/2
		return med
	else:
		return (x[int(len(x)/2)])


n = int(input("enter the number of digits: "))
print("enter "+str(n)+" digits:")
arr = list(map(float, input().split()[:n]))
print(arr)

print("the mean is: " + str(mean(arr)))
print("the median is: " + str(median(arr)))
print("the mode is: "+ str(int(stats.mode(arr)[0])))