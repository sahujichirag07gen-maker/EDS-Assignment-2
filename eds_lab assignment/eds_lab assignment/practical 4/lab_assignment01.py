# 4.2.1 Month with the highest total sales 
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

df['Date']= pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.to_period('M')
df['Sales']=df['Quantity']*df['Price']
monthly_sales = df.groupby('Month')["Sales"].sum()
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")



