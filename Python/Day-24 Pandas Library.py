import pandas as pd

#  Load CSV File
df = pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Python/day24_Employee_Data.csv")
print("\n=== Raw Data ===")
print(df.head())
print("\n=== Output ===")

# print("\n=== Bottom 5 Rows ===")
# print(df.tail())

# 2. Basic Information
# print("\nShape:", df.shape)
# print("Columns:", df.columns)
# print(df.info())
# print(df.describe())

# # 3. Clean Text data (Very Importnat)
# df["Employee_Name"] = df["Employee_Name"].str.strip().str.title() # Removing leading and trailing spaces
# print(df.head())

# # clean city Names
# df["City"]= df ["City"].str.strip().str.title()
# print(df.head())

# # Clean Department
# df["Department"] = df["Department"].str.strip().str.title()
# print(df.head())

# print("\n=== Cleaned Text Data in single line code ===")
# print(df[["Employee_Name", "City", "Department"]].head())

# # 4. Remove duplicates
# print("\nDuplicates Rows:", df.duplicated().sum())
# df = df.drop_duplicates

# print(df)

# # 5. Filter Data
# # Emloyees from Mumbai
# df["City"]= df ["City"].str.strip().str.title()
# mumbai_employees = df[df["City"] == "Mumbai"]
# # print(mumbai_employees)
# mumbai_employees.to_csv("C:/Users/ASUS/OneDrive/Desktop/Python/mumbai_employee.csv", index=False)

# # Employees with Salary > 60000
# high_salary = df[df["Salary"] > 60000]
# print(high_salary)

# # print("\nEmployees from Mumbai:", mumbai_emp.shape[0])
# print("Employees with Salary > 60000:", high_salary.shape[0])

# # 6. Sorting Data
# # sort by Salary (Desending)
# df_sorted_salary = df.sort_values("Salary", ascending=True)
# print(df_sorted_salary.head())

# # Sort by Joining Year
# df_sorted_year = df.sort_values("Joining_Year", ascending=False)
# print(df_sorted_year.head())

# 7. ADD new Cloumns
# # Salary Category
# df["Salary_Category"] = df["Salary"].apply(
#     lambda x: "High" if x > 60000 else "Medium" if x >= 50000 else "Low")
# print(df.head())
# # Experience Level
# df["Experience_Level"] = 2025 - df["Joining_Year"]
# print(df.head())

# 8. Group by Operations
# # Average Salary by Department
# avg_salary_dept = df.groupby("Department")["Salary"].mean()
# print(avg_salary_dept.head())

# # Total Salary by City
# df["City"]= df ["City"].str.strip().str.title()
# total_salary_city = df.groupby("City")["Salary"].sum()
# print(total_salary_city)

# # Employee Count by Department
# emp_count_dept = df.groupby("Department")["Employee_ID"].count()
# print(emp_count_dept.head())

# # 9. Exprot Cleaned data - Sort by Salary (Desecnding)
# df_sorted_salary = df.sort_values("Salary", ascending=False)
# # print(df_sorted_salary)    
# df_sorted_salary.to_csv("C:/Users/ASUS/OneDrive/Desktop/Python/employee_sorted_by_salary.csv", index=False)