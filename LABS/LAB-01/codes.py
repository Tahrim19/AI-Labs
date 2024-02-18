# # Write a Python program to convert temperatures to and from celsius
# temperature = float(input("Enter the temperature: "))
# print("Choose one.\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit")

# option = int(input("Enter your choice (1 or 2): "))

# if option == 1:
#     result = (temperature - 32)* 5/9
#     # print(f"{temperature} Fahrenheit is equal to %.2f Celsius" % result)
#     print("Temperature in Fahrenheit is: " , result)
# elif option == 2:
#     result = (temperature * 9/5) + 32
#     # print(f"{temperature} Celsius is equal to %.2f Fahrenheit" % result)
#     print("Temperature in Celcius is:  " , result)
# else:
#     print("Invalid Option")
   
   
   
   
    
# #  Write a Python program to swap 4 variables values (input four values)
# print("Before swapping")
# a, b, c, d = 2, 56, 78, 9
# print(a , b , c , d)
# print("After swapping")
# a , b , c , d = d , c , b , a
# print(a , b , c , d)



# # Write a Python program to count the number of strings where the string length is 2 or more and the 
# # first and last character are same from a given list of strings.
# L = ['abc', 'xyz', 'aba', '1221']
# length = len(L)
# count = 0
# if length > 0:  
#     for i in L:
#         if len(i) > 2 and i[0] == i[-1]:  
#             count = count + 1

# print("Count of strings meeting the specified condition:", count)




# # dir:
# str = 'hello world'
# print(str.upper())
# print(str.isalpha())
# print(str.replace('world' , 'WORLD'))


# # List:
# li = [92 , 85 , -2 , 100 , 7 , 0 , 55 , -45]
# li.sort()
# li.insert(2, 99)
# li.pop(4)
# print(li)





# L = ["APPLE", "MANGO", "ORANGE", "GRAPE", "STRAWBERRY", "PINEAPPLE"]
# result = []
# for i in L:
#     if len(i) > 5:
#         result.append(i.lower()) 
         
# print(result)



# L = [1,2,3,4,5,6,7,8,9] 
# indicesToRemove = [0,4,5]
# result = []
# for i in range(len(L)):
#     if i not in indicesToRemove:
#         result.append(L[i])  
    
# print(result)    




# # DICTIONARY

# dictionary = {"name": "John", "age": 25, "city": "New York"}

# print("Dictionary methods")
# print(dir(dictionary))


# help(dictionary.values)
# help(dictionary.pop)
# help(dictionary.clear)

# res = list(dictionary.values())
# print("After getting values: " , res)

# res = dictionary.pop('city')
# print("After Popping last key:" , dictionary)

# res = dictionary.clear()
# print("After Clearing: " , res)






# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# res = dic1.copy()  
# res.update(dic2)   
# res.update(dic3)   

# print("Concatenated Dictionary:\n", res)



def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1 


my_list = [2, 5, 8, 12, 16, 23, 38, 42]

target_element = int(input("Enter target element: "))

result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
