# this program wil demostrate functions

# single argument
def print_name(name):
    print(f'Name is: {name}')
    return 0

print_name('Gustavo')

myname = print_name('Pepe')

print(myname)

# multiples arguments
def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

# positional arguments: are based on its position
a=contact_card("Keith", 29, "Civic")
print(a)
# keyword argument: are based on a key
b=contact_card(age=29, car_model="Civic", name="Keith")
print(b)
# positional arguments always comes first than keyword arguments
c=contact_card("Keith", car_model="Civic", age="29")
print(c)
# so this lastone, results in error SyntaxError: positional argument follows keyword argument
#d=contact_card(car_model="Civic", age="29", "Keith")
#print(d)

# default arguments defines a value in the function itself, so argument can be ommited in function call
def can_drive(age, driving_age=16):
    return age >= driving_age

a=can_drive(15)
b=can_drive(16)
c=can_drive(21)
d=can_drive(16, driving_age=18)

print(str(a), str(b), str(c), str(d))