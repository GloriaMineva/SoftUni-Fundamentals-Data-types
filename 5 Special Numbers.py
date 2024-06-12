n = int(input())
# 1st method - convertion to list
#sum_of_digits = 0
# for current_digit in range(1, n + 1):
#     current_list = [int(i) for i in str(current_digit)]
#     sum_of_digits = sum(current_list)
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f'{current_digit} -> True')
#     else:
#         print(f'{current_digit} -> False')

# 2nd method - Integer Division and Modulo
# for current_digit in range(1, n + 1):
#     sum_of_digits = 0
#     digit = current_digit
#     while digit > 0:
#         sum_of_digits += digit % 10
#         digit = digit // 10
#
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#          print(f'{current_digit} -> True')
#     else:
#          print(f'{current_digit} -> False')

# 3rd method - slicing

for current_digit in range(1, n + 1):
    sum_of_digits = 0
    current_digit = str(current_digit)
    list_of_digits = [int(i) for i in current_digit[::-1]]
    sum_of_digits = sum(list_of_digits)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
          print(f'{current_digit} -> True')
    else:
          print(f'{current_digit} -> False')

