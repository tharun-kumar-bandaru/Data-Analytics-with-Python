# Create Sets
fruits = {"apple", "banana", "cherry", "Mango", "grapes","Mango", "apple"}
# print(fruits)

# # Add item
# fruits.add("orange")
# print(fruits)

# # Remove item
# fruits.discard("banana")
# print(fruits)

# # Set Operations
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print("Union:", A | B)  # Union
# print("Intersection:", A & B)  # Intersection
# print("Difference (A - B):", A - B)  # Difference
# print("Difference (B - A):", B - A)  # Difference
# print("Symmetric Difference:", A ^ B)  # Symmetric Difference
# # Remove duplicates from a list using sets
# cities = ["Mumbai", "Delhi", "Bangalore", "Mumbai", "Delhi"]
# unique_cities = set(cities)
# print(unique_cities)

# # Missing Values
# list1 = {"SQL", "Python", "Java", "C++"}
# list2 = {"Python", "JavaScript", "C#", "SQL"}
# missing = list2 - list1
# print("Missing items in list2:", missing)

# Common Values
list1 = {"SQL", "Python", "Java", "C++" }
list2 = {"Python", "JavaScript", "C#", "SQL"}
common = list1 & list2
print("Common items in both lists:", common)