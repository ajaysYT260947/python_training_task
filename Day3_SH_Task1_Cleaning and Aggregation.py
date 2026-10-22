import pandas as pd

# Load the CSV file
df = pd.read_csv("orders.csv", dtype={"order_id": str})

print("Original DataFrame:")
print(df)

# Find missing values
print("\nMissing values:")
print(df.isna().sum())

#  Find duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

#  Fill missing amount with the median
df["amount"] = df["amount"].fillna(df["amount"].median())

# Ensure correct data types
df["amount"] = pd.to_numeric(df["amount"])
df["order_id"] = df["order_id"].astype(str)

print("\nCleaned DataFrame:")
print(df)

print("\nData types:")
print(df.dtypes)

# Group by customer_id and aggregate
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print("\nCustomer-wise Aggregation:")
print(result)