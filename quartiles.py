
def median(arr):
	x = sorted(arr)
	if (len(x) % 2) == 0:
		y = (x[int((len(x)-1)/2)], x[int((len(x)+1)/2)])
		med = sum(y)/2
		return med
	else:
		return (x[int(len(x)/2)])

def quartiles(arr):
	q2 = median(arr)
	x = sorted(arr)
	if (len(x) % 2) == 0:
		q1 = median(x[:(int(len(x)/2))])
		q3 = median(x[(int(len(x)/2)):])
	else:
		q1 = median(x[:(int(len(x)/2))])
		q3 = median(x[(int(len(x)/2))+1:])
	return q1,q2,q3

n = int(input("enter the number of elements: "))
print("enter "+str(n)+" elements:")
ele = list(map(int, input().split()[:n]))
print(ele)
print("enter "+str(n)+" weights:")
freq = list(map(int, input().split()[:n]))
print(freq)
arr = [element for element, frequency in list(zip(ele, freq)) for _ in range(frequency)]
print(arr)
q1,q2,q3 = quartiles(arr)
print(float(q3-q1))



