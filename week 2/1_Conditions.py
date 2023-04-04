#the syntax for a condotions is as follows:
#if condition : 
#   code
#(^ Tab)
#if the condition is True then the code will execute


#exercise answer : 
username = input("enter username : ")
password = input("enter password : ")

if username == "wrong" and password == "ads sports":
    print("Connected to bank.")

if username != "wrong" or password != "ads sports":
    print("wrong password or username.")


#exercise answer : 
a = 3
b = 4
c = 5

#if a ** 2 + b ** 2 == c ** 2 [:]
#[TAB]print("This line should run for 3, 4, 5 but not for 4, 5, 6")
#[] <- was missing

if a ** 2 + b ** 2 == c ** 2:
    print("This line should run for 3, 4, 5 but not for 4, 5, 6")

print("This line should run anyway")