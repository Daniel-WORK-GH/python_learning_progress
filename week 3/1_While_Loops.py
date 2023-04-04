#while loops

#exercise answer : 
def ex1(num : int):
    i = 1
    while i <= num:
        print(i)
        i += 1


#exercise answer : 
def  collatz(num : int):
    while num != 1:
        print(num)
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    print(num)


welcome = """
Pick a demonstration : 
1.basic while printing 
2.collatz conjecture
"""

ex = input(f"{welcome}\nenter exercise : ")
num = int(input("enter number : "))

if ex == "1":
    ex1(num)
elif ex == "2":
    collatz(num)
else:
    print("invalid.")