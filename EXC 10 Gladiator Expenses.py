total_losts = int(input())
expenses = 0
shield_counter = 0
helmet, sword, shield, armor = float(input()), float(input()), float(input()), float(input())
for current_loss in range(1, total_losts + 1):
    if current_loss % 2 == 0:
        expenses += helmet
    if current_loss % 3 == 0:
        expenses += sword
        if current_loss % 2 == 0:
            expenses += shield
            shield_counter += 1
            if shield_counter % 2 == 0:
                expenses += armor
print(f'Gladiator expenses: {expenses:.2f} aureus')