total_char = int(input())
ascii_sum = 0
for i in range(total_char):
    current_letter = input()
    ascii_sum += ord(current_letter)
print(f'The sum equals: {ascii_sum}')