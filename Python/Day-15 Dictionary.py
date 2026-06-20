student = {"name":"TharunKumar", "age": 21, "city": "Ongole"}
# print(student)

# #  Accessing values
# print(student["name"])
# print(student["age"])

# # Adding and Updating values
# student["Marks"] = 85
# student["city"] = "Hyderabad"
# print(student)

# # Removing values
# student.pop("age")
# print(student)

# # Dictionary Mwthods
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))

# # Looping through a dictionary
# for key in student:
#     print(key, ":", student[key])

# # # Nested Dictionary
# employee = {
#     "emp1": {"name" : "Tharun", "city": "Ongole"},
#     "emp2": {"name" : "Kumar", "city": "Hyderabad"}
# }
# print(employee["emp1"]["name"])

# # Mapping wrong -> correct
# mapper = {
#     "teh": "the",
#     "recieve": "receive",
#     "adress": "address",
#     "definately": "definitely"
# }
# print(mapper["teh"])