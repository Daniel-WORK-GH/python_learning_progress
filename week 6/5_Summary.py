from operator import add

def group_by(f, itr):
    dic = {}
    for i in itr:
        key = f(i)
        if not key in dic.keys():
            dic[key] = []
        dic[key].append(i)
    return dic
print(group_by(len, ["hi", "bye", "yo", "try"]))

def zipwith(f, itr1, itr2, *itrs):
    return [
        f(itr1[i], itr2[i], *[x[i] for x in itrs]) for i in range(0, len(itr1))
    ]

print(zipwith(add, [1, 2, 3], [4, 5, 6]))
print(zipwith(max, (5, 4), (2, 5), (6, -6)))