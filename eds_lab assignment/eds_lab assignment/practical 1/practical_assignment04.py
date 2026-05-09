# 1.1.4 Reverse a number 
#write your code here...
n=int(input())
reverse=0
while n>0 :
	digit=n%10
	reverse= reverse*10+digit
	n=n//10
print(reverse)
