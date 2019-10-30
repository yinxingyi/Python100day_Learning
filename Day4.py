# ---------------------------------------------------------------
# print prime number within 0~100
# num = int(input('input a integer:'))

# for number in range(0,101):
#     for i in range(2, number):
#         if number%i == 0:
#             print("%d is a not prime number!" %number)
#             break
#         elif i == number-1:
#             print("%d is a prime number!" %number)

# --------------------------------------------------------------
#
# num = int(input("please enter a number:"))
#
# for x in range(2, num+2):
#     for x in range(0,x):
#         if x !=0:
#             print("*", end = '')
#             x= x-1
#     print()
#
# for i in range(num):
#     for j in range(num):
#         if j < num - i - 1:
#             print(" ", end='')
#         else:
#             print("*", end = '')
#     print()
#
# for i in range(num):
#     for _ in range(num - i - 1):
#         print(' ', end = '')
#     for _ in range(2*i+1):
#         print('*', end = '')
#     print()
#
# print out :
# *
# **
# ***
# ****
# *****
#     *
#    **
#   ***
#  ****
# *****
#     *
#    ***
#   *****
#  *******
# *********
# ----------------------------------------------------------------------
