#check if person is eligible for driving license
from datetime import date,datetime
print("Enter your name")
name = input()
print("Enter your date of birth")
dob = input()
def check(name,dob):
    age = date.today().year - int(dob)
    if age >= 18:
        return True
    else:
        return False

checker = check(name,dob)
if checker == True:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")