lines_to_follow = int(input())
left_bracket = 0
right_bracket = 0
for i in range(lines_to_follow):
    current_str = input()
    if current_str == '(':
        left_bracket += 1
    if current_str == ')':
        right_bracket += 1
    if left_bracket - right_bracket > 1 or right_bracket > left_bracket:
        print('UNBALANCED')
        exit()
if left_bracket == right_bracket:
    print('BALANCED')
else:
    print('UNBALANCED')