# 1.1.2 conditional calculation based on the number of digits
#write your code here...

n=int(input())
if(n>=1 and n<=9):
	print(n*n)
elif (n>=10 and n<=99):
	print(f"{n**0.5:.2f}")
elif (n>=100 and n<=999):
	print(f"{n**(1/3):.2f}")
else:
	print("Invalid")