#to get input from the user we will use the method 'input(string)'

#for example - exersice answer : 
fname = input("enter first name : ")
lname = input("enter last name : ")
bday = input("enter date of birth : ")

msg = "Hi " + fname + " " + lname + "! Your birthday is on " + bday
print(msg)


#exersice answer : 
w = float(input("enter width of box : "))
l = float(input("enter length of box : "))
h = float(input("enter height of box : "))

size = w * l * h
print(size)


#exersice answer : 
f = int(input("enter temperature in fahrenheit : "))
c = 5 / 9 * (f - 32)
print("converted to celcius :", c)


#exersice answer : 
name = input("enter your name : ")
age = int(input("enter your age : "))

print(str(name) + ", wait another " + str(90 - age) + " years.")