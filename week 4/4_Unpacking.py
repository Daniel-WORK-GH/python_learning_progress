#use * to unpack into arguments
#use ** to unpack by key(names) from dict
def print_treasure_location(x, y):
    print(f"{x}°N, {y}°E")

treasure_location = (36.671111, 65.808056)
print_treasure_location(*treasure_location) #<----


#exercise answer :
suspects = (
  {'name': 'Anne', 'evidences': ('derringer', 'Caesarea')},
  {'name': 'Taotao', 'evidences': ('derringer', 'Petersen House')},
  {'name': 'Pilpelet', 'evidences': ('Master Sword', 'Hyrule')},
)

def check_evidences(weapon, location):
    return weapon.lower() == 'derringer' and location.lower() == 'petersen house'

new_suspects = []
for dic in suspects:
    weapon, place = suspects['evidences']
    if check_evidences(weapon, place):
        new_suspects.append(dic['name'])

print(new_suspects)
