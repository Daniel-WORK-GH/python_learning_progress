#\n - line down
#\t - tab
#\', \" - ', "
#\\ - \
#write r before the string to not use special characters
#""" to handle a text with special cases
#fstring - print {variable values} in brackets
#string.strip() removes all spaces around the string
#string.strip(characters) removes all instences of x in character from the string
#string.find(substring) returns the index of the substring in the string, -1 if its not it the string
#string.index(substring) returns the index of the substring in the string, error if its not it the string
#string.lower() returs the string in lowercase
#string.count(value) count the nubmer of times {value} in seen inside of the string
#string.replace(start_val, end_val) replaces all reacurances of start_val with end_val
#string.split(str) splits the string into a list every {str} 
#list.join(by_val) joins an str list into a string with by_val between every list value
#string.startswith(value) returns true/false
#string.endsswith(value) returns true/false
#string.isalnum() returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
#string.isalpha() returns True if all the characters are alphabet letters (a-z).
#string.isdecimal() returns True if all characters in a string are decimal characters


#exercise answer :
print("With this faith we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day.\nThis will be the day when all of God's children will be able to sing with new meaning, \"My country 'tis of thee, sweet land of liberty, of thee I sing. Land where my fathers died, land of the Pilgrims' pride, from every mountainside, let freedom ring.\"")


#example
strange_string = '!@#$%!!!^&This! Is! Sparta!!!!!!!!!&^%$!!!#@!'
print(strange_string.strip('~!@#$%^&*'))


#example
strange = "This is a very long string which contains strange words, like ululation and lollygag."
print(strange.find("ululation"))
print(strange.index("lollygag"))

#example
i_love_to_eat = ['chocolate', 'fudge', 'cream', 'cookies', 'banana', 'hummus']
thing_to_join_by = ", "
print(thing_to_join_by.join(i_love_to_eat))


#exercise answer : 
gettysburg_address = """
Four score and seven years ago our fathers brought forth, on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we cannot dedicate—we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they here gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth. 
"""

list = gettysburg_address.replace('-', ' ').strip().split(' ')
n = len(list)
nation = list.count("nation")
great = list.count("great")
here = list.count("here")
we = list.count("we")
dedicated = list.count("dedicated")
total = nation + great + here + we + dedicated
print(f"total words : {n}\npercentage : {total / n}%")


#exercise answer : 
inp = input("enter a slogen : ")
inp = inp.replace("war", "peace")
inp = inp.replace("freedom", "slavery")
inp = inp.replace("ignorance", "strength")
print(inp)