import random
import string

password_len = int(input('enter desired password length: '))

letters = input('Include letters? (y/n): ').strip().lower()
numbers = input('Include numbers? (y/n): ').strip().lower()
symbols = input('Include symbols? (y/n): ').strip().lower()

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