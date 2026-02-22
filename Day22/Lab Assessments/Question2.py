import pandas as pd
import numpy as np

# 1️⃣ Load the CSV into a DataFrame
df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

# 2️⃣ Add new column "Total"
df["Total"] = df["Quantity"] * df["Price"]

print("\nData with Total column:")
print(df)

# 3️⃣ NumPy calculations
daily_sales = df["Total"].values   # convert to NumPy array

total_sales = np.sum(daily_sales)
average_daily_sales = np.mean(daily_sales)
std_dev_sales = np.std(daily_sales)

print("\nSales Analysis:")
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_daily_sales)
print("Standard Deviation of Daily Sales:", std_dev_sales)

# 4️⃣ Best-selling product (based on total quantity sold)
product_sales = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_sales.idxmax()

print("\nBest Selling Product:", best_selling_product