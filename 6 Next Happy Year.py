year = input()
# while True:
#     if year[0] != year[1] and year[0] != year[2] and year[0] != year[3] and\
#         year[1] != year[2] and year[1] != year[3] and year[2] != year[3]:
#         print(year)
#         break
#     else:
#         year = int(year)
#         year += 1
#         year = str(year)
year = input()
while True:
    if len(set(year)) == len(year):
        print(year)
        break
    else:
        year = int(year) + 1
        year = str(year)