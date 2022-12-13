import math  
import timeit
  
def isPrime(n):
	if n <= 1:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def fn():
	start = 1
	end = 2000000
	cnt = 0
	for i in range(start, end + 1, 1):
   		res = isPrime(i)
   		if res:
   			cnt += 1
	print("There are " + str(cnt) + " primes in the " + str(start) + "-" + str(end) + " range.")

if __name__ == "_main_":
	t = timeit.timeit(stmt=fn, number=1)
	print(t)