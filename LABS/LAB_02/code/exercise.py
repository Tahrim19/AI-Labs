# # # EXERCISE # 01:
# def volume(height,weight,depth):
#     volume = height*weight*depth
#     print(f"volume of cube is : {volume}")
#     if 1 <= volume <= 10:
#         print("Extra Small")
#     elif 11 <= volume <= 25:
#         print("Small")
#     elif 26 <= volume <= 75:
#         print("Medium")
#     elif 76 <= volume <= 100:
#         print("Large")
#     elif 101<= volume <= 250:
#         print("Extra-Extra Large")
#     else:
#         print("Extra-Extra Large")


# height = int(input("Enter height: "))
# weight = int(input("Enter weight: "))
# depth = int(input("Enter depth: "))
# volume(height , weight , depth)

# # EXERCISE # 02:
# def worker_efficiency(time_taken):
#     if 2 <= time_taken <= 3:
#         return "Highly Efficient"
#     elif 3 < time_taken <= 4:
#         return "Improve Speed"
#     elif 4 < time_taken <= 5:
#         return "Training Required"
#     elif time_taken > 5:
#         return "Leave the Company"
#     else:
#         return "Invalid Input"


# time_taken = float(input("Enter the time taken by the worker (in hours): "))
# efficiency = worker_efficiency(time_taken)
# print(f"The worker's efficiency is: {efficiency}")


# # EXERCISE # 03:
# def checkPassword(password):
#     if password == 'abc$123' or password == 'ABC$123':
#         print("Welcome!")
#     else:
#         print("I dont know you.")


# username = input("Enter username: ")
# password = input("Enter password: ")
# checkPassword(password)
        
        
        


# Scenario 1
# print("Countries in the set:")
# clist = ['Canada', 'USA', 'Mexico', 'Australia']
# for country in clist:
#     print(country)

# Scenario 2
# print("Counting from 0 to 100:")
# for i in range(101):
#     print(i, end=" ")
#     if (i + 1) % 10 == 0:
#         print()

# Scenario 3
# def table(number):
#     for i in range(1, 11):
#         result = number * i
#         print(f"{number} * {i} = {result}")
    
# num = int(input("Enter number: "))
# print(f"Multiplication Table of {num}")
# table(num)

# Scenario 4
# print("Number from 1 to 10 in backward order:")
# for i in range(10,0,-1):
#     print(f"{i}", end=" ")
    
# Scenario 5    
# print("Even numbers from 0 to 10:")
# for i in range(0, 11, 2):
#     print(f"{i}", end=" ")

# Scenario 6
# Using a loop to sum numbers from 100 to 200
sum = 0
for num in range(100, 201):
    sum += num

print(f"The sum of numbers from 100 to 200 is: {sum}")
