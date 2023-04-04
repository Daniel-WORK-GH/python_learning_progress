#id(variable-name) used to return a unique identification value of the object stored in the memory
#tuple vales cant be changed after assignment

#test 1
print("---example one---")
number = 100000
print("ID before: " + str(id(number)))
number = 123456
print("ID after: " + str(id(number)))

print("\n---example two---")
number = 100000
print("ID before: " + str(id(number)))
number = number + 1
print("ID after: " + str(id(number)))

print("\n---example three---")
print(f"ID of number ({number}): " + str(id(number)))
number2 = 100001
print(f"ID of number2 ({number2}): " + str(id(number2)))

print("\n---example four---")
my_list = ['It\'s', 'never', 'enough']
print(f"id() of my_list ({my_list}) before:\n\t" + str(id(my_list)))
my_list[2] = 'lupus'
print(f"id() of my_list ({my_list}) after:\n\t" + str(id(my_list)))