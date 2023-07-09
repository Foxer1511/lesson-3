# # #1 завдання
# # num1 = int(input("enter 1 digit = "))
# # num2 = int(input("enter 2 digit = "))
# # num3 = int(input("enter 3 digit = "))
# # user_select = int(input("enter 1 for max, enter 2 for min, enter 3 for avg = "))
# #
# # #v1
# #
# # if user_select == 1:
# #     if num1 > num2 > num3:
# #         print(num1)
# #     elif num2 > num3 > num1:
# #         print(num2)
# #     elif num3 > num2 > num1:
# #         print(num3)
# #     else:
# #         print("Equals!")
# # elif user_select == 2:
# #     if num1 < num2 < num3:
# #         print(num1)
# #     elif num2 < num3 < num1:
# #         print(num2)
# #     elif num3 < num2 < num1:
# #         print(num3)
# #     else:
# #         print("Equals!")
# # elif user_select == 3:
# #     print(f"Avg: {(num1 + num2 + num3) / 3}")
# #
# # #v2
# #
# # match user_select:
# #     case 1:
# #         if num1 > num2 > num3:
# #             print(num1)
# #         elif num2 > num3 > num1:
# #             print(num2)
# #         elif num3 > num2 > num1:
# #             print(num3)
# #         else:
# #             print("Equals!")
# #     case 2:
# #         if num1 < num2 < num3:
# #             print(num1)
# #         elif num2 < num3 < num1:
# #             print(num2)
# #         elif num3 < num2 < num1:
# #             print(num3)
# #         else:
# #             print("Equals!")
# #     case 3:
# #         print(f"Avg: {(num1 + num2 + num3) / 3}")
# #     case _:
# #         print("Error!")
# #
# #2 завдання
# num1 = int(input("enter 1 number = "))
# num2 = int(input("enter 2 number = "))
# math_action = input("Enter math action: + - * / ")
#
# match math_action:
#     case "+":
#         print(f"{num1} {math_action} {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} {math_action} {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} {math_action} {num2} = {num1 * num2}")
#     case "/":
#         if num2 != 0:
#             print(f"{num1} {math_action} {num2} = {num1 / num2}")
#         else:
#             print("Division by zero!!")
#     case _:
#         print("Error!!")
#!