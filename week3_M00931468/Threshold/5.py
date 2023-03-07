# Body Mass Index(BMI)

def pounds_to_kg(lb):
    return round((float(lb) * 0.45359237),5)

def inches_to_meters(height):
    return round((float(height) *0.0254),5)

def bmiCalculator():
    weight = pounds_to_kg(input('Enter your weight in pounds: '))
    height = inches_to_meters(input('Enter your weight in inches: '))
    bmi = (weight) / (height ** 2)
    
    if bmi < 18.5:
        print('You are Underweight')
    elif bmi >= 18.5 and bmi <= 25.0 :
        print('You are Normal')
    elif bmi > 25.0 and bmi <= 30 :
        print('You are Overweight')
    else:
        print('You are Obese')


def main():
    bmiCalculator()

main()

