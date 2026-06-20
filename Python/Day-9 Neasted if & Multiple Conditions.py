# Nested If
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You are eligible to vote.")
#     if age >= 21:
#         print("You are also eligible to drink alcohol.")
#     else:
#         print("You are not eligible to drink alcohol.")
# else:
#     print("You are not eligible to vote.") 



# Multiple Conditions (and)
age = int(input("Enter your age:"))
residence = input("Are you Indian?:")

if age >=18 and residence.lower() == "yes":
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")
17

# # Multiple Conditions (or)
# age = int(input("Enter your age:"))
# residence = input("Do you have licence:")

# if age >=18 or residence.lower() == "yes":
#     print("You are eligible to drive.")
# else:
#     print("You are not eligible to drive.")