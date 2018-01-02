num = raw_input()
num = int(num)
suma = 0

if num >= 0:
	for x in range(0, num + 1):
		suma += x
else:
	for x in range(num, 2):
		suma += x

print suma