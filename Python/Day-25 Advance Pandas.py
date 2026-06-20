import pandas as pd

#  Load CSV File
df = pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/Python/cleaned_employee_data.csv")
# print("\n=== Raw Data ===")
# print(df)
print("\n=== Output ===") 

# # Filtering
# df["City"] = df["City"].str.strip().str.title()  # Remove leading/trailing whitespace
# mumbai_emp = df[df["City"] == "Mumbai"]
# print(mumbai_emp)

# # High Salary
# high_salary = df[df["Salary"] > 60000]
# print(high_salary)

# # Multiple Conditions
# mumbai_high_salary = df[(df["City"] == "Mumbai") & (df["Salary"] > 60000)]
# print(mumbai_high_salary)

# mumbai_pune = df[(df["City"] == "Mumbai") | (df["City"] == "Pune")] 
# print(mumbai_pune)

# # Using .isin() for Multiple Values
# IT_and_Finance = df[df["Department"].isin(["IT", "Finance"])]
# print(IT_and_Finance)

# Advance Sorting
# df_sorted_salary = df.sort_values("Salary", ascending=False)

# # Sort by Department then salary
# df_sorted_multi = df.sort_values(["Department", "Salary"], ascending=[True, False])
# print(df_sorted_multi)

# # Group By Operations
avg_salary_dept = df.groupby("Department")["Salary"].mean()
# print(avg_salary_dept)

# # Total Salary by City
# total_salary_city = df.groupby("City")["Salary"].sum()
# print(total_salary_city)

# # Employee count by Department
# emp_count_dept = df.groupby("Department")["Employee_ID"].count()
# print(emp_count_dept)

# # Multiple Aggregations
# salary_stats = df.groupby("Department")["Salary"].agg(["mean", "min", "max", "count"])

# print("\nSalary Stats:")
# print(salary_stats)

# # Sort & Group By 
sorted_average_salary = avg_salary_dept.sort_values(ascending=False)
print("\nDepartment by Avg Salary:")
print(sorted_average_salary)


