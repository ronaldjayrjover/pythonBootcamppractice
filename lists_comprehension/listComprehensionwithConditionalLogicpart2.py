
'''
1. given 2 list [1,2,3,4] and [3,4,5,6], create a variable called answer, which is a new list that is the
intersection of the two. Your output should be [3,4].

2. given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2, which is a new list. should
be reversed and in lower case

'''

#Using list comprehensions(the more Pythonic way):

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
print(answer)
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
print(answer2)
#Without list comprehensions, things are a bit longer:

answer3 = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer3.append(x)
print(answer3)
answer4 = []
for name in ["Elie", "Tim", "Matt"]:
    answer4.append(name[::-1].lower())
print(answer4)

'''
For all the numbers between 1 and 100(including 100), create a variable called answer, which contains
a list with all the numbers that are divisible by 12
'''

answer5 = [val for val in range(1,100) if val % 12 == 0]
print(answer5)

'''
"Amazing" , create a variable answer which is a list containing all the letters from amazing but not the vowels
'''
answer6 = [char for char in "amazing" if char not in 'aeiou']
print(answer6)

#alternative, a lists within a list
# answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]]