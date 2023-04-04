# file.seek(pos) place pointer in new location {pos}
# file.tell() return the current pointer position
# file.read(count) read {count} bytes
# file.readline() read till \n or \0
# file.readlines() read all tiles into an array {with \n and eol}
# file.write(value) writes {valie} into the file
# file.flush() write all data saved in buffer into file
# file.close() stop using file
# with -resource- as -name: 
#   -code using -name- -
# ^ auto close file and the end
# ; 


#exercise answer : 
file = open('passwords.txt', 'r')

def is_password_common(password):
    file.seek(0)
    common_passwords = file.read().strip().split('\n')
    return password in common_passwords


password = input("enter a password : ")
if is_password_common(password):
    print("password is common.")
else :
    print("password isn't common.")

file.close()


#exercise answer : 
rating = 0
name = ""
with open('cereal.cvs', 'r') as file:
    lines = file.readlines()
    i = 1
    while i < len(lines):
        temp = lines[i].split('\t')
        r = float(temp[len(temp) - 1])
        n = temp[0]
        if r > rating:
            rating = r
            name = n
        i += 1

print(name)