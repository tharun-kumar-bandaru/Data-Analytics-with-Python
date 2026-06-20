import pandas as pd
from datetime import datetime

# Load CSV file
df = pd.read_csv("day24_Employee_Data.csv")

# # 1. Clean Employee_Name and City columns
# df["Employee_Name"] = df["Employee_Name"].str.strip().str.title()
# df["City"] = df["City"].str.strip().str.title()
# print(df.head())

# # 2. Remove duplicate rows
# df = df.drop_duplicates(subset=["Employee_ID"], keep="first")
# print(df)

# # 3. Add Experience column (Current Year - Joining_Year)
# current_year = datetime.now().year
# df["Experience"] = current_year - df["Joining_Year"]
# print(df)

# # Display cleaned dataframe
# print(df)

# # Optional: Save cleaned data to a new CSV
# df.to_csv("cleaned_employee_data.csv", index=False)