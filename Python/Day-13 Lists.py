# Create Lists
fruits = ["apple", "banana", "cherry"]
# print(fruits)

# # Indexing
# print(fruits[0])  # Output: apple
# print(fruits[- 1])  # Output: banana

# # Update List
# fruits[1] = "blueberry"
# print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# # Add items
# fruits.append("orange")
# fruits.insert(1, "Papaya")  
# print(fruits)  # Output: ['apple', 'Papaya', 'blueberry', 'cherry', 'orange']

# Remove items
# fruits.remove("cherry")  # Remove by value
# fruits.pop(0)  # Remove by index
# print(fruits)  # Output: ['apple', 'Papaya', 'cherry',

# # Slicing
# nums  = [10, 20, 30, 40, 50]
# # print(nums[4:5])  # Output: [20, 30, 40]
# print(nums[-4:-2])  # Output: [10, 20, 30]

# # Looping
# for f in fruits:
#     print(f)

# # Clean city names
# city = ["NEW York", "LoS AngELes", "ChiCAgo", "Houston", "Phoenix"  ]
# cleaned = []
# for c in city:
#     cleaned.append(c.strip().title())
# print(cleaned)

# # Replace wrong spellings
# wrong = ["Kolkatta", "bengluru"]
# fixed = []
# for w in wrong:
#     w = w.replace("Kolkatta", "Kolkata").replace("bengluru", "Bengaluru")
#     fixed.append(w)
# print(fixed)


# Extract years
codes = ["laptop-2024", "phone-2023", "tablet-2022"]
years = []
for code in codes:
    years.append(code[-4:])
print(years)  # Output: ['2024', '2023', '2022']