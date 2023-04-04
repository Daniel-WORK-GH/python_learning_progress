class Poll:
    def __init__(self, ques, options):
        self.ques = ques
        self.options = {o : 0 for o in options}

    def vote(self, option):
        if not (option in self.options):
            return False
        self.options[option] += 1
        return True

    def add_option(self, new_op):
        if (new_op in self.options):
            return False
        self.options[new_op] = 0
        return True

    def remove_option(self, option):
        if not (option in self.options):
            return False
        self.options.pop(option)
        return True

    def get_votes(self):
        lisdic = list(map(lambda x: (x, self.options[x]), self.options))
        sort = sorted(lisdic, key = lambda x : x[1], reverse=True)
        return sort
    
    def get_winner(self):
        return max(self.options, key=self.options.get)
    


def cast_multiple_votes(poll, votes):
    for vote in votes:
        poll.vote(vote)


bridge_question = Poll('What is your favourite colour?', ['Blue', 'Yellow'])
cast_multiple_votes(bridge_question, ['Blue', 'Blue', 'Yellow'])
print(bridge_question.get_winner() == 'Blue')
cast_multiple_votes(bridge_question, ['Yellow', 'Yellow'])
print(bridge_question.get_winner() == 'Yellow')
print(bridge_question.get_votes() == [('Yellow', 3), ('Blue', 2)])
bridge_question.remove_option('Yellow')
print(bridge_question.get_winner() == 'Blue')
print(bridge_question.get_votes() == [('Blue', 2)])
bridge_question.add_option('Yellow')
print(bridge_question.get_votes() == [('Blue', 2), ('Yellow', 0)])
print(not bridge_question.add_option('Blue'))
print(bridge_question.get_votes() == [('Blue', 2), ('Yellow', 0)])