# 2.2.1 Linear search technique 
n=input().split()
key=input()
i=0
found=False
while i<len(n):
	if n[i]==key:
		print(i)
		found=True
		break
	i+=1

if found==False:
	print("Not found")


