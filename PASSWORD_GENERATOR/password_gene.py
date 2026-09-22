import random
import string

while True:
    try:
        password_len = int(input('enter desired password length: '))
    except ValueError:
        print('Please enter a number')
        continue

    if password_len < 8:
        print('password\'s  length has to be 8 or greater')
        continue

    break

while True:
    letters = input('Include letters? (y/n): ').strip().lower()
    numbers = input('Include numbers? (y/n): ').strip().lower()
    symbols = input('Include symbols? (y/n): ').strip().lower()

    if letters not in ['y', 'n'] or  numbers not in ['y', 'n'] or symbols not in ['y', 'n']:
        print('Please make sure your answer is y or n')
        continue

    if letters == 'n' and numbers == 'n' and symbols == 'n':
        print('Please select at least one type of character!')
        continue

    break

character_pool = ''

if letters == 'y':
    character_pool += string.ascii_letters
if numbers == 'y':
    character_pool += (string.digits)
if symbols == 'y':
    character_pool += (string.punctuation)

random_choices = random.choices(character_pool, k=password_len)

generated_password = ''.join(random_choices)

print(generated_password)