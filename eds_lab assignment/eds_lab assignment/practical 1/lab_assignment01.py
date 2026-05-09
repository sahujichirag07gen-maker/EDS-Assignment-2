# 1.2.1 pass or fail 
n = int(input())
marks = list(map(int, input().split()))

# check if any subject is below 40
if min(marks) < 40:
	print("Fail")
else:
	average = sum(marks) / n
	print(f"Aggregate Percentage: {average:.2f}")

	if average > 75:
		print("Grade: Distinction")
	elif average >= 60:
		print("Grade: First Division")
	elif average >= 50:
		print("Grade: Second Division")
	elif average >= 40:
		print("Grade: Third Division")
		






