total_lines = int(input())
total_liters = 0
for i in range(total_lines):
    current_liters = int(input())
    total_liters += current_liters
    if total_liters > 255:
        print('Insufficient capacity!')
        total_liters -= current_liters
print(total_liters)