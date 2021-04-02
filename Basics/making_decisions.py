# # 3.1 Making decisions
# # 3.1.1.9
# largest_number = -9999999999
# number = int(input("Enter any number or enter -1 to exit: "))
# while number != -1:
#     if number == -1:
#         largest_number = number
#         exit()
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter any number or enter -1 to exit: "))
#
# # Find the largest number of all given numbers
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))
#
# largest_number = max(number1, number2, number3)
# print("The largest number of {},{},{} is {}.".format(number1, number2, number3, largest_number))

# 3.1.1.10 Lab: comparison operators and conditional execution
# flower_name = input("Enter Spathiphyllum if it is your favorite: ")
# if flower_name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever")
# elif flower_name == "spathiphyllum":
#     print("No - I was a big Spathiphyllum!")
# else:
#     print("It is Spathiphyllum! Not {}".format(flower_name))

# # 3.1.1.11 Lab: Essentials of the if-else statement
# income = float(input("Enter your annual income: "))
# if income <= 85528:
#     tax = (income * .18) - 556.02
# else:
#     tax = ((income - 85528) * .32) + 14839
#
# if tax <= 0:
#     tax = 0.0
#
# tax = round(tax, 0)
# print("The tax is : ", tax, "thallers")



