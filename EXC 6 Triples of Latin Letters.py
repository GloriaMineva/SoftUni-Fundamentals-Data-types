total_letters = int(input())
for i in range(97, 97 + total_letters):
    for j in range(97, 97 + total_letters):
        for k in range(97, 97 + total_letters):
            print(f'{chr(i)}{chr(j)}{chr(k)}')
