height = float(input('enter your height: '))

weight = float(input('enter your weight: '))

def bmi_calculator(weight, height):
    bmi = weight/ (height * height)
    print(f'yor bmi is: {bmi}')
    return