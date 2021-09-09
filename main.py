import random

IS_PRESENT = 1
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8

check_emp = random.randint(0,1)
if check_emp == IS_PRESENT:
    print("Employee is present and the wage is = " +str (WAGE_PER_HOUR * FULL_DAY_HOURS))
else:
    print("Employee is absent")