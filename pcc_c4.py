# c4

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = [value**2 for value in range(1, 11)]
print(squares)

# slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

# copy
players_pure_copy = players[:]  # pure copy using slice, two separate lists
players_not_copy = players      # not copy, just reference

