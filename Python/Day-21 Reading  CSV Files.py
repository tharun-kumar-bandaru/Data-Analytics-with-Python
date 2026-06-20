import csv

# #  Reader entire CSV file 
# with open("C:/Users/ASUS/Downloads/Day21_Order_Data.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# # Read with DictReader
# with open("C:/Users/ASUS/Downloads/Day21_Order_Data.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["Order_ID"],  row["Payment_Type"])

# # Total sales
# total_sales = 0
# with open("C:/Users/ASUS/Downloads/Day21_Order_Data.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         total_sales += int(row["Price"])*int(row["Quantity"])
# print(f"Total Sales:", total_sales)

# Filter by City
mumbai = []
with open("C:/Users/ASUS/Downloads/Day21_Order_Data.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["City"] == "Mumbai":
            mumbai.append(row)
print(mumbai)