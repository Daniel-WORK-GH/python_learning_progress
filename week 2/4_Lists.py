#value in [list]
#value not in [list]

#exersice answer : 
def sort(list):
    n = len(list)
    for i in range(n):
        for j in range(i + 1, n):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
        
judges = ['Esther Hayut', 'Miriam Naor', 'Asher Grunis', 'Dorit Beinisch', 'Aharon Barak']
sort(judges)
print(judges)

#exersice answer : 
ice_cream_flavours = ['chocolate', 'vanilla', 'pistachio', 'banana']
flavour = input("enter your favorite flavour")
print(flavour in ice_cream_flavours)

