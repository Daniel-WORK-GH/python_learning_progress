import random
import turtle
from calendar import prmonth as print_calendar 
import datetime

def create_password():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = list(letters + letters.lower()) 
    length = random.randint(12, 20)
    password = ""
    for i in random.choices(chars, k=length):
        password += i
    return password

print(f"new password : {create_password()}")


def turtle_example():
    turtle.speed(1000)

    for i in range(400):
        turtle.forward(50 + i)
        turtle.right(91)

    turtle.done()

current_date = datetime.datetime.now()
print_calendar(current_date.year, current_date.month)

#exercise answer : 
def cards():
    cards = list(range(0, 52))
    players = [[],[],[],[]]
    while len(cards) > 0:
        i = random.choice(cards)
        players[random.randint(0,3)].append(i % 13 + 1)
        cards.remove(i)

    for i in range(0, 4):
        players[i] = sum(players[i])
    
    print(players)
    print(players.index(max(players)))


#exercise answer : 
def final(date : str):
    now = str(datetime.datetime.now())
    date2 = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
    date1 = datetime.date(int(now[0:4]), int(now[5:7]), int(now[8:10]))
    delta = date2 - date1
    print(delta)


#exercise answer : 
def vinigret(date1 : str, date2 : str):
    date_1 = datetime.date(int(date1[0:4]), int(date1[5:7]), int(date1[8:10]))
    date_2 = datetime.date(int(date2[0:4]), int(date2[5:7]), int(date2[8:10]))
    rnd_date = datetime.date(
        random.randint(date_1.year, date_2.year),
        random.randint(date_1.month, date_2.month),
        random.randint(date_1.day, date_2.day)
    )
    print(rnd_date.isoweekday() == 1)
vinigret("2020-02-20", "2023-02-24")