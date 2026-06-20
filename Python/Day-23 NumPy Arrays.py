import numpy as np

print("=== Creating Arrays ===")
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(arr) 

# print("\n=== Indexing & slicing ===")
# print(arr[1])
# print(arr[0:6])

# # print("\n=== Vectorized Operations ===")
# print(arr + 10)
# print(arr*2)
# print(arr**2)

# print("\n=== Numpy Fuctions ===")
# print(arr.sum())
# print(arr.mean())
# print(arr.min(), arr.max())

print("\n=== Data Cleaning Example ===")
# data = np.array([10, -20, 30, -40, 50, -60, 70, -80, 90, -100])
# clean = data[data >= 0]
# print(clean)

# marks =np.array([80, 90, -1, 75, -1, 60])
# marks[marks == -1] = marks [marks != -1].mean() # Replacing Average fof non negative 
# print(marks)

cities = np.array(["muMBai", "deLHi", "banGAlore", "hYderAbad", "chenNai", "mumbai"])
cities = np.char.strip(cities) # Removing leading and trailing spaces
cities = np.char.title(cities) # Converting to lowercase
print(cities)

