import math

def exampels():
    def silly_generator():
        a = 1
        yield a
        b = a + 1
        yield b
        c = [1, 2, 3]
        yield c

    our_generator = silly_generator()

    print(next(our_generator))
    print(next(our_generator))
    print(next(our_generator))

    #itirate
    our_generator = silly_generator()
    for item in our_generator:
        print(item)

    #convert to list
    our_generator = silly_generator()
    items = list(our_generator)
    print(items)

    #my range
    def my_range(upper_limit):
        current_number = 0
        while current_number < upper_limit:
            yield current_number
            current_number = current_number + 1


    our_generator = my_range(1000)
    for number in our_generator:
        print(number)

#exercise answers : 
def bikoret(id : str):
    b = 0
    for i, c in enumerate(id):
        cnt = int(c) * (i % 2 + 1)
        b += cnt % 10 + cnt // 10
    return math.ceil(b / 10) * 10 - b

def generate_bikoret():
    for i in range(0, 1_0000_0000):
        id = str(i).zfill(8)
        print(id)
        yield bikoret(id)

def print_all_bikort():
    gen = generate_bikoret()
    for i in gen:
        print(i)


def get_divisors(x : int):
    lis = []
    for i in range(1, x):
        if x % i == 0:
            lis.append(i)
    return lis

def print_shusi():
    i = 1
    last = 6
    while True:
        divisors = get_divisors(i)
        if sum(divisors) == i:
            last = i
        i += 1
        yield last

def print_all_rolls():
    gen = print_shusi()
    for i in gen:
        print(i)