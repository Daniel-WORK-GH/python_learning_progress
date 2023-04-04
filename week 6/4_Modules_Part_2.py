#pip :
#   install
#   uninstall
#   show {name} - show data on {name}
#   search {name}
#   list - show all installed modules

import names
import random_address
import random

def gen_random_phone():
    return "05" + "".join(str(random.randint(0,9)) for x in range(0,7))

def create_people(n):
    return {
        x : {
            "email" : f"{x.replace(' ','')}@gmail.com",
            "address" : random_address.real_random_address(),
            "phpne" : gen_random_phone()
        } for i in range(0, n) 
        for x in [names.get_full_name()]
    }

print(create_people(1))