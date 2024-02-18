# # TASK:03
# def divide(divisor , dividend):
#     if divisor == 0:
#         print("cannot divide by zero")
#         return
    
#     quotient = 0
#     remainder = 0;
    
#     while dividend >= divisor:
#         dividend = dividend - divisor
#         quotient = quotient + 1

    
#     remainder = dividend
    
#     print("Quotient: " , quotient)
#     print("Remainder: " , remainder)
    

# dividend = int(input("Enter Dividend: "))
# divisor = int(input("Enter Divisor: "))
# divide( divisor, dividend)


# # TASK:02
# def BMI(weight , height):
#     bmi = weight / height**2
#     print(f"BMI is: {bmi}")
#     if bmi <= 18.5:
#         print("Underweight")
#     elif 18.5 <= bmi <= 24.9:
#         print("Normal Weight")
#     elif 25.0 <= bmi <= 39.9:
#         print("Over Weight")
#     else:
#         print("Obese")
    

# weight = float(input("Enter Weight in Kilograms: "))
# height = float(input("Enter Height in Meters: "))
# BMI(weight,height)


# TASK:01
def integer_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

number = int(input("Enter a positive integer: "))
if 1 <= number <= 3999:
    roman_numeral = integer_to_roman(number)
    print(f"The Roman numeral for {number} is: {roman_numeral}")
else:
    print("Input out of range. Please enter a positive integer between 1 and 3999.")

