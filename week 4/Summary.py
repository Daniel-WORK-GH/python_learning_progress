#answer : 
def get_election_results():
    dic = {}
    with open("elections.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip("\n")
            dic[line] = dic.get(line, 0) + 1
    return dic

def get_passing_parties(dic : dict):
    passing = []
    for key, value in dic.items():
        if value >= 35340:
            passing.append(key)
    return passing

def get_passing_votes(dic : dict):
    passing = get_passing_parties(dic)
    cnt = 0
    for party in passing:
        cnt += dic[party]
    return cnt

def get_election_seats(dic : dict):
    passing = get_passing_parties(dic)
    seats_dic = {}
    for party in passing:
        seats_dic[party] = round(dic[party] / 2077.775)
    return seats_dic

def election():
    dic = get_election_results()
    cnt = get_passing_votes(dic)
    seats_dic = get_election_seats(dic)
    print(f"votes for passing parties : {cnt}")
    print(f"nubmer of seats for each party : ")
    for key, value in seats_dic.items():
        print(f"{key} : {value}")
