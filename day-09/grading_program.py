def grading_program():
    
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99, 
        "Draco": 74,
        "Neville": 62,
    }

    student_grades = {}

    for k, v in student_scores.items():
        if v >= 91:
            student_grades[k] = 'Outstanding'
        elif v >= 81:
            student_grades[k] = 'Exceeds Expectations'
        elif v >= 71:
            student_grades[k] = 'Acceptable'
        else:
            student_grades[k] = 'Fail'

    print(student_grades)
            
if __name__ == '__main__':
    grading_program()
