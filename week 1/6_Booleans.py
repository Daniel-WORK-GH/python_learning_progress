#in boolean logic, python contains the usual == != > >= < <=
#in addion to another key word 'in' (substring in string)

#different numeric types can be compared with each other 
#like int == float, but cant with other types like string
#it depends of each variable type and its constraints

#in python we will use True and False


#exersice answer : 
#5 == 3 -> False
#1 != 1 -> False
#5 > 3 -> True
#5 < 3 -> False
#'hello' == 'Hello' -> False
#'MARIO' == 'MARIO ' -> False
#1.5 == 1 -> False
#1.0 == 1 -> True
#1 == 1.0 -> True
#5 != 7 - 2 -> False
#5 >= 5.0 -> True
#'5' > '24' -> True, but should be False
#'Hell' in 'Hello' -> True
#'hell' in 'Hello' -> False
#'tom' in 'to master' -> False
#'2' in '20' -> True
#2 in '20' -> Error, sould be string in string, not int in string


#exersice answer : 
age = int(input("enter age : "))
print(age >= 25)