'''

map :
    a standard function that accepts at least 2 arguments, a function and an iterable
    iterable - something that can be iterated over
    runs the lamda for each value in the iterable and returns a map object which can be converted into another
        data structure
'''
nums = [2,4,6,8,10]
doubles = map(lambda x: x*2, nums)
print(list(doubles))

peeps = ["jay", "ron", "nald"]
people = list(map(lambda peoples: peoples.upper(), peeps))
print(people)


'''
increment exercise

I define the function decrement_list that accepts a list called l
Inside, I call map and pass in a lambda and the list, l
The lambda returns n-1 for each n in the list
The last step is to convert the return value of map to a list
Remember, map returns a <map object>, not a list
Oh, and finally we return the result!

decrement_list([1,2,3]) # (0,1,2)
decrement_list([20,14,18]) # (19,13,17)
'''

def decrement_list(l):
    return list(map(lambda n: n-1, l))

'''
filter
    there is a lambda for each value in the iterable
    returns filter object which can be converted into other iterables
    the object contains only the values that return true to the lambda
'''
l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, l ))
print(evens)

names = ["jay", "nald", "borg"]
a_names = list(filter(lambda n: n[1]=='a', names))
print(a_names)

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(),
                     filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]



