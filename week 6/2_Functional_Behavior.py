import time

def examples():
    #example : 
    def add(num1, num2): return num1 + num2
    def subtract(num1, num2): return num1 - num2
    def multiply(num1, num2): return num1 * num2
    def divide(num1, num2): return num1 / num2

    functions = [add, subtract, multiply, divide]
    for function in functions:
        print(function(5, 2))

    #example : 
    numbers = [(2, 4), (1, 4, 2), (1, 3, 5, 6, 2), (3, )]
    sums = map(sum, numbers)
    print(tuple(sums))


    #exercise answer : 

def get_fname(str : str):
    return str.split(' ')[0]

full_names = ['fname lname', 'john doe']
fnames = list(map(get_fname, full_names))
print(fnames)


def is_palindrome(pali : str):
    rev = list(pali)
    rev.reverse()
    rev = "".join(rev)
    return pali == rev

words = ["abcba", "ashsard", '124421']
print(tuple(filter(is_palindrome, words)))


#exercise answers : 
def my_filter(func, itr):
    for i in itr:
        if func(i):
            yield i

print(tuple(my_filter(is_palindrome, words)))


def get_positive_numbers():
    return list(map(int, input("enter numbers : ").split(',')))

#print(get_positive_numbers())


def timer(f, *params):
    ct = time.time()
    time.sleep(1) #for testing
    f(*params)
    return time.time() - ct

print(timer(print, "hello world"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))