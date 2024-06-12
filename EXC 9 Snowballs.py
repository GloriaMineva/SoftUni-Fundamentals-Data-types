total_balls = int(input())
highest_value = 0
winner_weight = 0
winner_time = 0
winner_quality = 0
for i in range(total_balls):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_value = (weight / time) ** quality
    if current_value > highest_value:
        highest_value = current_value
        winner_weight = weight
        winner_time = time
        winner_quality = quality
print(f'{winner_weight} : {winner_time} = {int(highest_value)} ({winner_quality})')