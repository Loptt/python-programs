numbers = raw_input()
i = 0
num1 = ''
num2 = ''

while numbers[i] != ' ':
	num1 = num1 + numbers[i]
	i = i + 1

for x in xrange(i,len(numbers)):
	num2 = num2 + numbers[x]

answer = int(num1) + int(num2)

print answer
