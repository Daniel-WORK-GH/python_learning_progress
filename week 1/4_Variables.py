#there are several rules for naming variables:
#1.the name will contain only the letters a-z and numbers 0-9
#2.the name cant start with a number
#
#in addition there are several consensus on nameing variables:
#1.the name will be in lowercase and words will be separated by '_'
#2.the name should reflect the porpouse of the variable

#exercise answer : 
a = 5
MyBirthday = '12/07/1995'
mybirthday = '12/07/1995'
pizza_radius = 5.3
pizza = 3
#pizza radius = 2.7 the name contains a space so it breaks rule 1
#pizza's_price = 2 the name contains ' so it breaks rule 1
#5_pizza_price = 30 the name starts with a number so it breaks rule 2
my_name = "Yam Mesicka"
your_name = '4Tomer Gavish'

#exercise answer : 
boxes_bought = 5
units_per_row = 10
units_per_col = 4

total = boxes_bought * units_per_row * units_per_col
print(total)


#exercise answer : 
#part 1
pool_length = 50
pool_width = 25
route_length = (pool_length ** 2 + pool_width ** 2) ** 0.5

print(route_length)

#part 2 
pool_length = pool_length * 2
pool_width = pool_width + pool_length
pool_size = pool_length * pool_width

print(pool_size)


#exercise answer : 
name = "daniel"
msg = "congrats"
combined = name + ' ' + msg
print(combined)