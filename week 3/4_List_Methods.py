# list.append(value) add {value} to list
# list.pop() remove last element from list
# list.extend(list_2) add to list the values from list_2
# list.count(value) return number of times {value} is in list
# list.index(value) return index of {value} or error if not in list
# list.remove(value) remove the first instance of {value} from list
# list.sort() sort the list
# list.inser(index, value) insert {value} at {index} := list = list[:index + 1] + value + list[index + 1:];

#exercise answer : 
def flatten_rsort_list(var):
    """EXAMPLE : 
    FOR [[1, 2, 3], [4, 5, 6]]
    RETURN [6, 5, 4, 3, 2, 1]
    """
    ret = []
    i = 0
    while i < len(var):
        ret.extend(var[i])
        i += 1
    ret.sort()
    ret.reverse()
    return ret
    
var = [[1, 2, 3], [4, 5, 6]]
var = flatten_rsort_list(var)
print(var)
    