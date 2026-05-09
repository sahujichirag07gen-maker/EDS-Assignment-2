# 4.1.3 student information 
import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# write your code here..
print("First five rows:")
print(data.head(5))

print("Average age:",round(data['Age'].mean(),2))

print("Students with a grade up to B")
print(data[data['Grade'].isin(['A','B'])])