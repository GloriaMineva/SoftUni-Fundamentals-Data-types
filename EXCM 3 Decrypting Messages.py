key = int(input())
lines_to_follow = int(input())
secret_word = ''
for current_index in range(lines_to_follow):
    letter = input()
    secret_word += chr((ord(letter) + key))
print(secret_word)