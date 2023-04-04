#functions act as a 'black box' that recieves an input and 
#returns an output, syntax :
#def -function name-(-input variables-):
#   -some code-
#   -optional return-


#exercise answer : 
carbs = int(input("enter carbs : "))
protein = int(input("enter protein : "))
fats = int(input("enter fats : "))
calories = 4 * carbs + 4 * protein + 9 * fats
print("calories =", calories)


#exercise answer : 
def calulate_calories():
    carbs = int(input("enter carbs : "))
    protein = int(input("enter protein : "))
    fats = int(input("enter fats : "))
    calories = 4 * carbs + 4 * protein + 9 * fats
    return calories

#calulate_calories()


#exercise answer : 
def get_speed():
    distance = 5
    hours = float(input("how many hours : "))
    speed = distance / hours
    print(speed)
    return speed

def maraton():
    distance = 42.195
    speed = get_speed()
    time = distance / speed
    print(time <= 3)

maraton()


#exercise answer : 
def reverse_num(num):
    return num % 10 * 10 + num // 10

#not recommended \/
print(reverse_num(int(input("enter number to reverse : "))))


#hard exercise answer : 
correct_code = 4812
code_1 = 4
code_2 = 8
code_3 = 1
code_4 = 2

#check if a digit is part of the code
def check_digit(digit):
    return digit == code_1 or digit == code_2 or digit == code_3 or digit == code_4

#check how many digits in a number are part of the code
def check_number(num):
    digit_1 = num // 1000
    digit_2 = num % 1000 // 100
    digit_3 = num % 100 // 10
    digit_4 = num % 10 
    cnt = 0
    if check_digit(digit_1):
        cnt += 1
    if check_digit(digit_2):
        cnt += 1
    if check_digit(digit_3):
        cnt += 1
    if check_digit(digit_4):
        cnt += 1
    return cnt

#check if code correct / print how many correct digits
def check_code_once():
    code = int(input("enter code : "))
    if code == correct_code:
        return True
    correct = check_number(code)
    print("number of correct digits :", correct)

#give 3 tries to guess the code
def check_code():
    return check_code_once() or check_code_once() or check_code_once()

if check_code():
    print("Correct guess!")
else:
    print("Incorrect")

