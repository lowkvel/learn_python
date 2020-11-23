# input and while

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

age = int(input("How old are you? "))
print((age + 5)%3)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

