# files and exceptions

# read the whole file
with open('README.md') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# read the file line by line
with open('README.md') as file_object:
    for line in file_object:
        print(line.rstrip())

# read the file and make a list of lines from it
with open('README.md') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# write to an empty file
with open("WRITEME.md", 'w') as file_object:    # w for write, r for read, a for append
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# append to an existed file
with open("WRITEME.md", 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# exceptions
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        #print("You cant divide by 0!")
        pass
    else:
        print(answer)

def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
        print(contents.rstrip())
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', 'WRITEME.md']
for filename in filenames:
    count_words(filename)

# storing data
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename, 'r') as f:
    numbers = json.load(f)
print(numbers)

filename = 'username.json'
try:
    with open(filename, 'r') as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

