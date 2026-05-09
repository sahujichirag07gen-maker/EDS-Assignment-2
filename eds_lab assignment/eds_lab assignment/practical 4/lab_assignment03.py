# 4.2.3 city that solds the most products 
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# write the code..
city_wise_sell = df.groupby('City')['Quantity'].sum().reset_index()
best_city = city_wise_sell.loc[city_wise_sell['Quantity'].idxmax()]

print(f"City sold the most products: {best_city['City']}")
# # Display the result
# print(f"City sold the most products: {best_city}")
