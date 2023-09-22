from datetime import datetime

# printing muna
father_name = input("Enter your father's name: ")
birthplace = input("Enter your father's birthplace: ")
birthday_str = input("Enter your father's birthday (YYYY-MM-DD): ")

# for conversion of birthday string to datetime object
birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

# calculate age
current_year = datetime.now().year
father_age = current_year - birthday.year

# display father's info
print("\nFather's Information:")
print(f"Name: {father_name}")
print(f"Birthplace: {birthplace}")
print(f"Birthday: {birthday.strftime('%Y-%m-%d')}")
print(f"Age: {father_age} years")