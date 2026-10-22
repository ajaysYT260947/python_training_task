import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("employees.csv")

print("Full DataFrame:")
print(df)

# Display the first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

df.info()

print(df.describe())

print(df[["name", "salary"]])

print(df.loc[df["city"] == "Chennai", "name"])

print(df.iloc[0:3, 1:3])

#Filter employees with salary above 50000
high_salary = df[df["salary"] > 50000]

print("\nSalary above 50000:")
print(f"{len(high_salary)} employees")
print(high_salary)

it_employees = df[df["department"] == "IT"]

print("\nIT Department:")
print(it_employees["name"].to_list())
print("Count:", len(it_employees))