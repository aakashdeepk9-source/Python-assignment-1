#Python
# Task 1 Perform basic Mathematical Operations
num1=float(input("5: "))
num2=float(input("10: "))
addition=num1+num2
substraction=num1-num2
multiply=num1*num2
if num2 !=0:
    division=num1/num2
else:
    division='underfined(cannot divide by zero)'
print(f'addition: {addition}')
print(f'substraction: {substraction}')
print(f'multiply: {multiply}')
print(f'division: {division}')
