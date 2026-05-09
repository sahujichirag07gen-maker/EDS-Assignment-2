# 2.1.1 List operations 
# write the code..
list=[]

while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")

	a=int(input("Enter choice: "))

	if a==1:
		v=input("Integer: ")
		if v.isdigit()==True:
			list.append(int(v))
			print("List after adding:",list)
		else:
			print("Invalid input")

	elif a==2:
		if len(list)==0:
			print("List is empty")
		else:
			f=int(input("Integer: "))
			if f in list:
				list.remove(f)
				print("List after removing:",list)
			else:
				print("Element not found")

	elif a==3:
		if len(list)==0:
			print("List is empty")
		else:
			print(list)

	elif a==4:
		break

	else:
		print("Invalid choice")
		



