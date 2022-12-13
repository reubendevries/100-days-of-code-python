height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

def bmi_calculator(a,b):
    return int(float(b) / (float(a ** 2)))

if __name__ == '__main__':
    ans = bmi_calculator(height, weight)
    print(ans)