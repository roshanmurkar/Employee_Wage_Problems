import random

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

emp_attendence = {
    IS_PRESENT_FULL_DAY :
    "Employee is present for full time and the wage is = "+str(WAGE_PER_HOUR * FULL_DAY_HOURS),
    IS_PRESENT_PART_TIME:
    "Employee is present for part time and wage is = "+str (WAGE_PER_HOUR * PART_TIME_HOURS),
    IS_ABSENT:
    "Employee is absent"
    }

check_emp = random.randint(0,2)
print(emp_attendence.get(check_emp))