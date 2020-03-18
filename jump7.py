for i in range(1,101):
	if i%7==0  or i%10==7:
		continue
	elif i>=10 and i//10==7:
		continue
	print(i)

