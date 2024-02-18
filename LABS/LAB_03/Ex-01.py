# 1-
square = lambda a: a**2
cube = lambda a: a**3
    
given_list = [1,2,3,4,5,6]

squared = []
cubed = []

for i in given_list:
    squared.append(square(i))
    cubed.append(cube(i))
    
print("Original list: " , given_list)
print("Squared list: " , squared)
print("Cubed list: " , cubed)

    
    

# 2-
starts_with_char = lambda s, c: s.startswith(c)

given_string = input("Enter a string: ")
given_char = input("Enter a character to check if the string starts with it: ")

result = starts_with_char(given_string, given_char)

if result:
    print(f"The string '{given_string}' starts with the character '{given_char}'.")
else:
    print(f"The string '{given_string}' does not start with the character '{given_char}'.")



# 3-
from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

# Extract year, month, date, and time
year =  current_datetime.year
month = current_datetime.month
day = current_datetime.day
time = current_datetime.time()

# Print the extracted information
print("Current Year:", year)
print("Current Month:", month)
print("Current Date:", day)
print("Current Time:", time)
