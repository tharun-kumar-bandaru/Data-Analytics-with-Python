# def greet():
#     print("Hello, welcome to the world of functions!")
# greet()

# def welcome (name):
#     print("Welcome", name)
# welcome("Tharun")

# def add(a, b):
#     print("Sum:", a + b)
#     print("Difference:", a - b)
#     print("Product:", a * b)
# add(5, 10)


# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# result = multiply(add(5, 10), 2)
# print(result)

# def clean_text(text):
#     return text.strip().title()
# cleaned_text = clean_text("   hello world! welcome to python programming.   ") 
# print(cleaned_text)

# def fix_city(city):
#     city.strip().lower()
#     city = city.replace("mombai", "mumbai" )
#     city = city.replace("kolkatta", "kolkata" )
#     return city.title()

# print(fix_city("Mombai"))

# def get_year(code):
#     return code[-4:]
# print(get_year("EMP-2024"))

# def is_valid_email(email):
#     return "@" in email and "." in email
# print(is_valid_email("test@gmail.com"))

# def total_salary(basic, bonus):
#     return basic + bonus
# print(total_salary(50000, 10000))

# def stats(nums):
#     return min(nums), max(nums), sum(nums) / len(nums)
# print(stats([10, 20, 30, 40, 50]))

# def clean_list(values):
#     cleaned = []
#     for v in values:
#         cleaned.append(v.strip().title())
#     return cleaned

# print(clean_list(["  apple ", "banana ", " CHERRY", " mango"]))