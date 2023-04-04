import random


def interleave(*args):
    ret = []
    for x in args:
        for i in x:
            ret.append(i)
    return ret

print(interleave('abc', [1, 2, 3], ('!', '@', '#')))

def add_inventory(inv : dict, **items):
    for key, value in items.items():
        inv[key] = inv.get(key, 0) + value
    return inv
    
print(add_inventory({'cheese': 2, 'milk': 1}, cheese=3, chocolate=5))

def bday_paradox():
    classes : list[list] = []
    cnt = 0
    for i in range(0, 10_000):
        classes.append([])
        for j in range(0, 23):
            leap_year = random.randint(1,4) % 4 % 3 % 2
            rnd = random.randint(1, 365 + leap_year)
            if classes[i].count(rnd) == 1:
                cnt += 1
                break
            classes[i].append(rnd)
        yield f"{cnt} out of {i}"

def call_bday_paradox():
    gen = bday_paradox()
    for x in gen:
        print(x)

call_bday_paradox()
#about 5000 of 10000 so 50% like in the experiment