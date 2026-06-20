# # String Functions
# text = "banana"
# print(text.count("a"))  # Count occurrences of 'a'

# print("hello.py".endswith(".py"))  # Check if string ends with '.py'

# print("Sales_Report.csv".startswith("Sales"))  # Check if string starts with 'Sales'

# print("1233".isdigit())
# print("12.34".isdigit())
# print("abc".isdigit())
# print("123abc".isdigit())

# print("Line1\nLine2\nLine3")  # Newline character

# print("Line1\tLine2\tLine3".splitlines())  # Tab character


# #  List Functions
# nums = [5, 2, 7, 1, 4]
# nums.sort
# print(nums)  # Sort the list

# fruits = ["apple", "banana", "cherry", "Mango", "grapes"]
# print(sorted(fruits))  # Sort the list without modifying original

# marks = [85, 92, 78, 90, 88]
# print(max(marks), min(marks), sum(marks))  # Maximum value

# mylist = [1,2,1,3,1]
# print(mylist.count(1))  # Count occurrences of 1
# print(mylist.index(3))  # Find index of first occurrence of 3   

# a = [1, 2]
# b = [3, 4]
# a.extend(b)  # Extend list a with elements of b
# print(a)

# Number Functions
# print(round(3.98, 0))  # Round to 2 decimal places
# print(abs(-5))  # Absolute value
# print(pow(2, 3))  # Power function
# print(divmod(10, 3))  # Quotient and remainder
# print(sum([5,5,5], 5))

# # Practical Examples
# products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"]
# clean = [p.strip().lower() for p in products]  # Clean product names
# clean.sort()
# print(clean)

# emails = ["rohit@gmail.com","sneha@yahoo.com"]
# domains = [mail[mail.find("@") + 1:] for mail in emails]  # Extract domains
# print(domains)

# mobiles = ["9836543210", "987654SD10", "12345"]
# valid = [m for m in mobiles if m.isdigit() and len(m) == 10]  # Validate mobile numbers
# print(valid)