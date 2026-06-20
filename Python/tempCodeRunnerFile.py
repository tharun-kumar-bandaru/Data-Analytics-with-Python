# Employee count by Department
emp_count_dept = df.groupby("Department")["EmployeeID"].count()
print(emp_count_dept)