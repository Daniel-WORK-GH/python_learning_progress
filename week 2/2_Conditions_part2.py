#if we need to write the following code:
#if condition:
#   -something
#if not(condition):
#   -something else
#
#we can simplify it to:
#if condition:
#   -something
#else:
#   -something else

#in addition instead of:
#if condition:
#   -something
#if not(condition) and other_condition:
#   -something else
#
#we can write:
#if condition:
#   -something
#elif other_condition:
#   -something else

#exercise answer : 
my_username = "wrong"
my_password = "ads sports"
manager_username = "admin"
manager_password = "is trator"

username = input("enter username : ")
password = input("enter password : ")

if username == my_password and password == my_password:
    print("connected to your bank.")
elif username == manager_username and password == manager_password:
    print("connected to managers bank.")
else:
    print("invalid password or username")


#exercise answer : 
a = int(input("enter first number : "))
b = int(input("enter second number : "))
op = input("enter operation : ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '**':
    print(a ** b)
else:
    print("wrong input")
    

#exercise answer : 
salary = int(input("input salary : "))

val1 = 6310
val2 = 9050 
val3 = 14530  
val4 = 20200  
val5 = 42030  
val6 = 54130

tax = 0

if salary > val6:
    tax = tax + 0.50 * (salary - val6)
if salary > val5:
    tax = tax + 0.47 * (salary - val5)
if salary > val4:
    tax = tax + 0.35 * (salary - val4)
if salary > val3:
    tax = tax + 0.31 * (salary - val3)
if salary > val2:
    tax = tax + 0.20 * (salary - val2)
if salary > val1:
    tax = tax + 0.14 * (salary - val1)

tax = tax + 0.10 * salary

print("tax :", tax)
