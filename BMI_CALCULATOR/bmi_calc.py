height = float(input('enter your height: '))
weight = float(input('enter your weight: '))

def bmi_calculator(weight, height):
    bmi = weight/ (height * height)
    print(f'yor bmi is: {bmi}')
    return

bmi = bmi_calculator(weight, height)

if bmi < 18.5:
    print(f'yor bmi is: {bmi}, Underweight')
elif 18.5 <= bmi < 25:
    print(f'yor bmi is: {bmi}, Healthy Weight')
elif 25 <= bmi < 30:
    print(f'yor bmi is: {bmi}, Overweight')
elif 30 <= bmi < 35:
    print(f'yor bmi is: {bmi}, Obesity, Class 1 Obesity')
elif 34 <= bmi < 40:
    print(f'yor bmi is: {bmi}, Obesity, Class 2 Obesity')
else :
    print(f'yor bmi is: {bmi}, Obesity, Class 3 Obesity(Severe Obesity')