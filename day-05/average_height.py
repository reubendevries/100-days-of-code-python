# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


#Write your code below this row 👇

def average_height(list):
    
    sum_of_height = 0
    x = 0
    for i in list:
        sum_of_height += int(i)
        x += 1
    return round( (sum_of_height / x) )

if __name__ == '__main__':
    ans = average_height(student_heights)
    print(ans)