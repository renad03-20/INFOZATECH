import random
import string


def get_password_length():
    while True:
        try:
            password_len = int(input('Enter desired password length: '))

            if password_len < 8:
                print("Password's length has to be 8 or greater")
                continue

            return password_len

        except ValueError:
            print('Please enter a number')


def get_character_choices():
    while True:
        letters = input('Include letters? (y/n): ').strip().lower()
        numbers = input('Include numbers? (y/n): ').strip().lower()
        symbols = input('Include symbols? (y/n): ').strip().lower()

        if letters not in ['y', 'n'] or numbers not in ['y', 'n'] or symbols not in ['y', 'n']:
            print('Please make sure your answer is y or n')
            continue

        if letters == 'n' and numbers == 'n' and symbols == 'n':
            print('Please select at least one type of character!')
            continue

        return letters, numbers, symbols


def generate_password(password_len, letters, numbers, symbols):
    character_pool = ''

    if letters == 'y':
        character_pool += string.ascii_letters

    if numbers == 'y':
        character_pool += string.digits

    if symbols == 'y':
        character_pool += string.punctuation

    random_choices = random.choices(character_pool, k=password_len)

    return ''.join(random_choices)


def main():
    saved_passwords = []

    while True:
        password_len = get_password_length()

        letters, numbers, symbols = get_character_choices()

        generated_password = generate_password(
            password_len,
            letters,
            numbers,
            symbols
        )

        print(f'Generated password: {generated_password}')

        saved_passwords.append(generated_password)

        again = input('Generate another password? (y/n): ').strip().lower()

        if again != 'y':
            break

    print('\nSaved passwords:')

    for password in saved_passwords:
        print(password)


main()