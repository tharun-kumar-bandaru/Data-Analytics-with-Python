# # 1 Reading full file
# with open("C:/Users/ASUS/OneDrive/Desktop/Python/Sample.txt") as file:
#       print(file.read())

# # 2 Reading line by line
# with open("C:/Users/ASUS/OneDrive/Desktop/Python/Sample.txt") as file:
#       for line in file:
#             print(line.strip()
#                   .title())  # Remove leading/trailing whitespace
  
# #  3 Writing to a file
# with open("notes.txt", "w") as file:
#         file.write("This is a Day-20 sample note.\n")
#         file.write("File handling in Python is easy.")


# #  4 Appending to a file
# with open("notes.txt", "a") as file:
#         file.write("Appending new conent.\n")

# # Cleaning data in file
# cleaned = []
# with open("sample.txt") as file:
#       for line in file:
#             cleaned.append(line.strip().title())
# with open("cleaned_output.txt", "w") as file:
#       for city in cleaned:
#             file.write(city + "\n")

# # Counting lines in a file
# count = 0
# with open("sample.txt") as file:
#      for _ in file:
#            count += 1
# print(f"Total lines:", count)