# abs(number) - return absolute value of number
# print(f"{value:>6}") - make sure value is printed using 6 characters
# > - align to the right
# ^ - align to the middle
# < - align to the left
# max(list), min(list) 
# sum(list)
# round(float number)
# eval(str) run python code from str
# sorted(iterable) sort an iterable type
# sorted(iterable, reverse=True) sort an iterable type
# sorted(iterable, key=len) run key() on value in the iterable
#   and sort by value
# chr(number) convert number to char
# ord(char) convert char to nubmer
# enumerate(list) attach a number to each value in list
# ;

#copy list using list2 = list1[:]

#exercise answer : 
max_n = int(input("enter number : "))
print(sum(range(0, max_n + 1)))


#example : 
paintings = ['Mona Lisa', 'The Creation of Adam', 'The Scream', 'The Starry Night']
artists = ['Leonardo da Vinci', 'Michelangelo', 'Edvard Munch', 'Vincent van Gogh']

zipped_values = zip(paintings, artists)
print(list(zipped_values))

artists_from_paintings = dict(zip(paintings, artists))


#exercise answer : 
dic = {}
def count_words(file_name : str):
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            words = line.split(' ')
            for i in range(len(words)):
                words[i] = words[i].strip("'.,\n").lower()
                word = words[i]
                if(word != ''):
                    dic[word] = dic.get(word, 0) + 1

count_words("war-and-peace.txt")

cnt_max = 0
cnt_min = 100000000
word_max = ""
word_min = ""

for w, c in dic.items():
    if c > cnt_max:
        word_max = w
        cnt_max = c
    if c < cnt_min:
        word_min = w
        cnt_min = c

print(f"max : {word_max} => {cnt_max}")
print(f"max : {word_min} => {cnt_min}")