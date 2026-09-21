from datetime import datetime

def main():
    bmi_reading = load_readings()

    while True:
        print('*----****----*')
        print('1. Calculate BMI')
        print('2. View past readings')
        print('3. exit')
        print('*----****----*')

        option = input('Enter your choice: ')

        if option == '1':
            bmi = calculate_reading()
            if bmi is not None:
                bmi_reading.append(bmi)
                save_readings(bmi_reading)

        elif option == '2':
            show_readings(bmi_reading)

        elif option == '3':
            print("Exiting.")
            save_readings(bmi_reading)
            break

        else:
            print('Please select a valid option!')

def bmi_calculator(weight, height):
    bmi = weight / (height * height)
    return bmi

def get_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Healthy Weight'
    elif bmi < 30:
        return 'Overweight'
    elif bmi < 35:
        return 'Obesity, Class 1'
    elif bmi < 40:
        return 'Obesity, Class 2'
    else:
        return 'Obesity, Class 3'

def calculate_reading():
    try:
        height = float(input('enter your height: '))
        weight = float(input('enter your weight: '))
    except ValueError:
        print("Invalid input!")
        return None

    if height<= 0 or weight<= 0: 
        print('Height and weight must be greater than 0.')
        return None

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bmi = bmi_calculator(weight, height)
    category = get_category(bmi)

    print(f'your BMI is: {bmi:.2f}')
    print(f'Category: {category}')

    return f'{current_date}, {bmi:.2f}, {category}'

def show_readings(bmi_reading):
    print('\nBMI Readings')
    for i , bmi in enumerate(bmi_reading, start=1):
        print(i, '*', bmi)

def save_readings(bmi_reading):
    with open('bmi_reading.txt', 'w') as file:
        for bmi in bmi_reading:
            file.write(str(bmi) + '\n')

def load_readings():
    try:
        with open('bmi_reading.txt', 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    main()