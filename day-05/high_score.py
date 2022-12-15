student_scores = input('input a list of student scores: ').split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
def high_score(lst):

    high_score = 0
    for i in lst:
        if i >= high_score:
            high_score = 0
            high_score += i
        else:
            pass
    return f'The highest score in the class is: {high_score}'

if __name__ == '__main__':

    ans = high_score(student_scores)
    print(ans)