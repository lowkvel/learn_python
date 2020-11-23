# c1
# changing case in a string
message = "hello PYTHON world"
print(message)          # original string
print(message.title())  # in title case
print(message.upper())  # in upper case
print(message.lower())  # in lower case

# using variable in a string
fname = "ada"
lname = "lace"
fname = f"Hello, {fname} {lname}."  # f for format
print(fname.title())

# whitespaces(tabs, newlines), striping
print("\ttest")
print("\ntest")
message = "   test  asdf\tasdf    "
print(message)
print(message.strip())      # strip all
print(message.lstrip())     # strip from left side
print(message.rstrip())     # strip from right side

# multiple assignment
a, b, c = 1, 2, 3

# constant
THE_CONSTANT = 999

