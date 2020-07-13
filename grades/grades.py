import math
def sufix_ret(grade,value):
    grade_zero = int(value/10)*10    
    grade_three = grade_zero+3
    grade_seven = grade_zero+7
    if value<60:
        suffix = ''
    elif value>=grade_seven or value==100:
        suffix='+'
    elif grade_three<=value<grade_seven:
        suffix = ''
    else:
        suffix = '-'
    return "{}{}".format(grade,suffix)

def switch(value,sufix):
    procent = value
    if procent<60:
        grade = 'F'
    elif 60<=procent<70:
        grade = 'D'
    elif 70<=procent<80:
        grade = 'C'
    elif 80<=procent<90:
        grade = 'B'
    else:
        grade = 'A'
    return sufix_ret(grade,value) if sufix else grade

def percent_to_grade(procent,*,suffix=False,round=False):
    if round:
        procent = math.floor(procent) if int(str(procent)[-1])<5 else math.ceil(procent)   
    return switch(procent,suffix)


def calculate_gpa(grades):
    dict_gpa = {'A+':4.33
        ,'A': 4.00
        ,'A-': 3.67
        ,'B+': 3.33
        ,'B': 3.00
        ,'B-': 2.67
        ,'C+': 2.33
        ,'C': 2.00
        ,'C-': 1.67
        ,'D+': 1.33
        ,'D': 1.00
        ,'D-': 0.67
        ,'F': 0.00}
    return sum(dict_gpa[g] for g in grades)/len(grades)
