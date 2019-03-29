'''
sorted - returns a new sorted list from the items in the iterable
'''
numbers = [6,2,3,1,5]
print(sorted(numbers))
print(numbers) #its not change
print(sorted(numbers, reverse=True))

print(sorted((2,3,5,1,4)))
print(sorted(('k','l','m','c')))

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "colors": "teal", "pet": "dog"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
print(sorted(users, key=len)) # it will count how many keys then it will sort from shorted to longest
print(sorted(users, key=lambda user: user['username']))
print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))

'''
max
    return the largest item in an iterable or the lasgest of two or mote arguments
min
    opposite    
'''
print(max(2,3,44))
print(max('a','b','d'))
print(max("hello world"))

print(min(2,3,44))
print(min('a','b','d'))
print(min("hello world")) #its blank because the least is space

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
print(min(len(name) for name in names)) # 3

# find the longest name itself
print(max(names, key=lambda n:len(n))) #Ollivander

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
print(min(songs, key=lambda s: s['playcount'])) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
print(max(songs, key=lambda s: s['playcount'])['title']) #YMCA

