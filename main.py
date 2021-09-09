import random

IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

check_emp = random.randint(0,2)
if check_emp == IS_PRESENT_FULL_DAY:
    print("Employee is present for full time and the wage is = "+str(WAGE_PER_HOUR * FULL_DAY_HOURS))
elif check_emp == IS_PRESENT_PART_TIME:
    print("Employee is present for part time and wage is = "+str (WAGE_PER_HOUR * PART_TIME_HOURS))
else:
    print("Employee is absent")