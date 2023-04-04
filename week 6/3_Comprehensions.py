def mini_ex():
    #ex :
    numbers = [1, 2, 3, 4, 5]
    numbers = [n * n for n in numbers]
    print(numbers)

    #ex : [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    numbers = [(i, i + 1) for i in range(1,6)]
    print(numbers)

    #ex : 
    numbers = {i for i in range(0,1001) if i % 3 == 0 and i % 7 == 0}
    print(numbers)


#exercise answers : 
def words_length(sentence : str):
    return [len(w) for w in sentence.split(' ')]

print(words_length("Toto, I've a feeling we're not in Kansas anymore"))


def get_letters():
    return [
        chr(w) for w in range(66,122) if w != 90 and w != 97 and chr(w).isalpha()
    ]

print(get_letters())


def count_words (text : str):
    words = [''.join([x for x in w if x.isalpha()]) for w in text.split(' ')]
    dic = {word : len(word) for word in words}
    return dic

text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

print(count_words(text))


def full_names(fnames : list[str], lnames : list[str], minlen = 0):
    return [
        f"{f} {l}" for f in fnames
            for l in lnames 
            if len(f"{f}{l}") >= minlen
    ]
    
first_names = ['avi', 'moshe', 'yaakov']
last_names = ['cohen', 'levi', 'mizrahi']

print(full_names(first_names, last_names, 10))