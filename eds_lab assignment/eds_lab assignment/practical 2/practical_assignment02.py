# 2.1.2 Dictionary operation 
# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# write your code here...
print("Original Dictionary:",student)
key=int(input())
value=input()
student[key]=value
print("After Insertion:",student)
key2=int(input())
value2=input()
if key2 in list(student.keys()):
	student[key2]=value2
print("After Update:",student)
key3=int(input())
if key3 in list(student.keys()):
	student.pop(key3)
print("After Deletion:",student)
print("Traversing Dictionary:")
for k in student:
	print(k,':',student[k])