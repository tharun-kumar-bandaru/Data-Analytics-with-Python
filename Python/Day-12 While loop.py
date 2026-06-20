# # Basic While Loop
# i = 1
# while i <= 10:
#     print(i) 
#     i += 1

# # Countdown
# n = 10
# while n > 0:
#     print(n)
#     n -= 1

# # 3 ASK user until valid input
# num = ""
# while not num.isnumeric():
#     num = input("Enter a number: ")
#     print("Enter only number")
# print("You entered:", num)

# #  4 Loop through list
# items = ["Pen", "Pencil", "Eraser", "Sharpener"]
# i = 0
# while i < len(items):
#     print(items[i])
#     i += 1

# # 5 Using Break
# x = 1
# while x <= 10:
#     print(x)
#     if x == 8:
#         break
#     x += 1

# # 6 Using Continue  
# y = 0
# while y < 18:
#     y += 1
#     if y % 2 == 1:
#         continue
#     print(y)   

# 7 Password  System (Advance)
password = ""
attempts = 0
while password != "admin@123" and attempts < 3:
    password = input("Enter the password: ")
    atttempts += 1
    if password == "admin@123":
      print("Access Granted")
    else:
      print("Worng Password TRy Again, Attempt Count:", attempts)
      if attempts == 3:
           print("Access Denied")
 