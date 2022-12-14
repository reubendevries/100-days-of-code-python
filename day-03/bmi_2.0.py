height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

def bmi_calculator(a,b):
    
    bmi = round( ( b / ( a ** 2 ) ) )
    if bmi <= 18.5:
        return f'Your BMI is {bmi}, you are underweight'
    elif bmi <= 25:
        return f'Your BMI is {bmi}, you have a normal weight.'
    elif bmi <= 30:
        return f'Your BMI is {bmi}, you are slightly overweight.'
    elif bmi <= 35:
        return f'Your BMI is {bmi}, you are obese.'
    elif bmi > 35:
        return f'Your BMI is {bmi}, you are clinically obese.'

if __name__ == '__main__':
    ans = bmi_calculator(height, weight)
    print(ans)