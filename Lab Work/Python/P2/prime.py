# Prime Number Checker
flag = 0
n = int(input('Please Enter the Number: '))
if n != 1 : 
	if (n % 2) != 0:
		for x in range(3,(int(n/2) + 1),2):
			if (n % x) == 0 :
				flag = 1
				break
		if(flag == 0) :
			print('{0} is a Prime Number'.format(n))
		else :
			print('{0} is not a Prime Number'.format(n))
	else:
	   print('{0} is not a Prime Number'.format(n))
else :
	print('{0} is not a Prime Number'.format(n))