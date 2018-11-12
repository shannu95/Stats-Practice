import math

def mean(arr):
	avg = sum(arr)/len(arr)
	return avg

def stddev(arr, avg):
	sigma = 0
	for x in arr:
		sigma+=math.pow((x-avg),2)
		sdev = math.sqrt((sigma)/len(arr))
	return sdev

n = int(input("enter the number of digits: "))
print("enter "+str(n)+" digits:")
arr = list(map(float, input().split()[:n]))
avg = mean(arr)
print("the mean is: " + str(avg))
print("the standard deviation is: " + str(round(stddev(arr, avg),1)))