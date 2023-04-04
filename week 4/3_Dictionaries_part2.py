#del delete key-value pair in dict
#dict.pop() return value and del the pair
#dict.update(dict2) merge two dicts into one

loved_animals = {'Alice': 'Cat', 'Achiles': 'Tortoise'}
del loved_animals['Achiles']
print(loved_animals)


#exercise answer : 
lis = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4}]
merged_dict = {}
for dic in lis:
    merged_dict.update(dic)
print(merged_dict)


#exercise answer : 
students = {
    'nick' : {
        'test' : [80, 78, 90, 64],
        'hw' : [46, 99, 85, 90, 100]
    },
    'richard' : {
        'test' : [90, 92, 87, 99],
        'hw' : [88, 77, 94, 66, 96]
    },
    'sid' : {
        'test' : [66, 6, 66, 6],
        'hw' : [100, 100, 100, 100, 100]
    },
    'david' : {
        'test' : [96, 92, 91, 78],
        'hw' : [80, 77, 74, 71, 68]
    }
}

def avarage_of_list(lis : list) : 
    sum = 0
    for i in lis: sum += i
    return sum / len(lis)

def calc_grade_avg(tests_avg : int, hw_avg : int):
    return tests_avg * 0.8 + hw_avg * 0.2

def calc_final_grades(students : dict):
    for student, grades in students.items():
        tests_avg = avarage_of_list(grades['test'])
        hw_avg = avarage_of_list(grades['hw'])
        grade = calc_grade_avg(tests_avg, hw_avg)
        students[student].update({'final' :[grade]})

calc_final_grades(students)
print(students)
