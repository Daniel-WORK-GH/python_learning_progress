import random

def function(default : int = 1, *parameters):
    print(parameters)
    print(type(parameters))
    print('-' * 20)

#exercise answer : 
def create_path(*args):
    if not args:
        return None
    strr = args[0] + ":"
    for x in args[1:]:
        strr += "\\" + x
    return strr


def function2(**kwargs):
    print(kwargs)
    print(type(kwargs))


#exercise answer :
def my_format(string : str, **args):
    for key, value in args.items():
        string = string.replace("{"+key+"}", value)
    return string


#final exercises in a row : 
def avg(*args):
    if args == None:
        return None
    return sum(args) / len(args)


def join(*args : (list), sep='-'):
    if args == None:
        return None
    new = args[0].copy()
    for x in args[1:]:
        new.extend([sep] + x.copy())
    return new 


def get_recipe_price(prices : dict, optionals : list = None, **ingredients):
    price = 0
    for key, value in ingredients.items():
        price += prices.get(key, 0) * value / 100
    return price