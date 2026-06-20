# # String Methods (Very Imporant)

text1="        Hello python learns        "

# # Remove Spaces
# print("Original text:", text1)
# print("Remove spaces:", text1.strip())  # Remove spaces from both sides
                                       
# # Convert to Uppercase
# print("Uppercase:", text1.upper()
#                         .strip())        #rtrip() is used to remove spaces from right side
#                                          #ltrip() is used to remove spaces from left side

# # Convert to Proper Case
# print("Proper Case:", text1.title()
#                         .strip())


# # Convert to Lowercase
# print("Lowercase:", text1.lower()       
#                         .strip())


# # Replace Text
# print("Replace Text:", text1.replace("python", "data analyst")
#                         .strip())

# # Count Occurrence of a letter in word
# print("Count of o :", text1.count("o"))


# # Check if texts strat with somthing
# print("Starts with H:", text1.strip().startswith("Hello"))

# # Check if only numbers are present in data 
# mobile_number = "9876543210"
# print("Is digit:", mobile_number.isdigit())

# msg = "Welcome to python programming"

# # Split string into list of words
# words=msg.split()
# print("Split words:", words)


# # Join back woth hyphen
# joined_msg="-".join(words)
# print("Joined message:", joined_msg)

# # Find postion of letter 
# print("Position of p:", msg.find("p"))  # Returns index of first occurrence of "p"

# Extract domain from email
email = "student@example.com"
domain = email[email.find("@")+1:]
print("Domain:", domain)

# Advanced Example: Clean Price (Remove Special Characters)
# Example: "Price: 3500/-" -> "3500"
price_text = "Price: 3500/-"
clean_price = price_text.replace("Price: ", "").replace("/-", "").strip()
print("Clean Price:", clean_price)


# Ask ChatGpt comman used in Strin methods  