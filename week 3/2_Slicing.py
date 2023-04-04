#exercise answer : 
def okey_remove_numbers(s : str):
    new_s = ""
    i = 0
    while i < len(s):
        if(s[i].isalpha()):
            new_s += s[i]
        i += 1

    return new_s
 
def horrible_remove_numbers(s : str):
    i = 0
    while i < 10:
        s = s.replace(f"{i}", "")
        i += 1

    return s


#exercise answer : 
hello = "Hello World"
result = hello[6:] + hello[5:3:-1] + "f " + hello[:5]
print(result)


#exercise answer : 
pokemons = """
#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False
2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False
3,Venusaur,Grass,Poison,525,80,82,83,100,100,80,1,False
4,Charmander,Fire,,309,39,52,43,60,50,65,1,False
5,Charmeleon,Fire,,405,58,64,58,80,65,80,1,False
6,Charizard,Fire,Flying,534,78,84,78,109,85,100,1,False
7,Squirtle,Water,,314,44,48,65,50,64,43,1,False
8,Wartortle,Water,,405,59,63,80,65,80,58,1,False
9,Blastoise,Water,,530,79,83,100,85,105,78,1,False
10,Caterpie,Bug,,195,45,30,35,20,20,45,1,False
11,Metapod,Bug,,205,50,20,55,25,25,30,1,False
12,Butterfree,Bug,Flying,395,60,45,50,90,80,70,1,False
13,Weedle,Bug,Poison,195,40,35,30,20,20,50,1,False
14,Kakuna,Bug,Poison,205,45,25,50,25,25,35,1,False
15,Beedrill,Bug,Poison,395,65,90,40,45,80,75,1,False
16,Pidgey,Normal,Flying,251,40,45,40,35,35,56,1,False
17,Pidgeotto,Normal,Flying,349,63,60,55,50,50,71,1,False
18,Pidgeot,Normal,Flying,479,83,80,75,70,70,101,1,False
19,Rattata,Normal,,253,30,56,35,25,35,72,1,False
20,Raticate,Normal,,413,55,81,60,50,70,97,1,False
"""

list_of_strs = pokemons.strip("\n#").split('\n')
result = []
i = 1
while i < len(list_of_strs):
    list_of_strs[i] = list_of_strs[i].split(',')
    j = 1
    temp = []
    while j < len(list_of_strs[i]):
        if list_of_strs[i][j].isdecimal():
            temp += [int(list_of_strs[i][j])]
        else:
            temp += [list_of_strs[i][j]]
        j += 1
    result += [temp]
    print(result[len(result) - 1])
    i += 1
