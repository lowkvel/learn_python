# functions

# normal functions
def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('jesse')
greet_user('god')

# functions with default values
def describe_pet(animal_type, pet_name = "temp"):   # default value of pet_name is given
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# functions with returned value
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
print(get_formatted_name('jimi', 'hendrix'))

# function with optional parameters
def get_formatted_name(first_name, last_name, middle_name=''):  # optional parameter 
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name('john', 'hooker', 'lee'))

# arbitary number of arguments
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# arbitary number of keyword arguments
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

