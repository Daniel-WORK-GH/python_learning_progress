# for loops
# can be used as a for-each and as a regular for
# for v1,v2,v3 in tuple_list;

def ex1(path : list):
    end_x, end_y = 0, 0
    for x, y in path:
        end_x += x
        end_y += y 
    return (end_x, end_y)

path = [(1, 5), (6, -2), (4, 3)]
print(ex1(path))