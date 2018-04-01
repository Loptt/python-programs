import time
import threading

def calcSquare(numbers):
	print("Calculating square numbers")

	for n in numbers:
		time.sleep(0.2)
		print("square:", n*n)

def calcCube(numbers):
	print("Calculating cube numbers")

	for n in numbers:
		time.sleep(0.2)
		print("cube:", n*n*n)

array = [2,3,8,9]
start = time.time()

thread1 = threading.Thread(target=calcSquare, args=(array,))
thread2 = threading.Thread(target=calcCube, args=(array,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done in ", time.time()-start, " seconds")