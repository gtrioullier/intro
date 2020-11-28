# this program will demostrate loops

# while loop infinito
# it has no sense in any program
# that's why it will remain commented out
#while True:
#    print('looping')

# while loop with stop
count = 0
while count < 5:
    print('looping')
    count += 1

# while loop with stop, showing counter
count = 0
while count <= 5:
    print('looping: ' + str(count))
    count +=1

# while loop with conditionals
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    count += 1

# while loop with break
count = 0   # 0 is considered an even number
while count < 10:
    if count % 2 == 0 and count == 6:
        break
    elif count %2 == 0:
        count += 1
    print(f"We're counting odd numbers, up to 6: {count}")
    count += 1

# for loop
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

# for loop with conditionals
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)

# for loop, unpacking tuple
point = (2.1, 3.2, 7.6)
for values in point:
    print(values)

# for loop, unpacking dict keys
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in ages:
    print('clave: ' + key)

# for loop, unpacking dict keys and values
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key,value in ages.items():
    print(f'clave:  {key}  value:  {value}')

# for loop, split a string
for letter in "my_string":
    print(letter)
