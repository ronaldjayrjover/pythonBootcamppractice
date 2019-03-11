#clear - clears all the keys and values in a dictionary

instructor = {
    "name": "jay",
    "age": 36,
    "state": "quezon",
    "color": "blue"
}
#
#print(instructor.clear())
##/Users/ronaldj/Documents/pythonbootcamp/pythonBootcamppractice/converge/bin/python /Users/ronaldj/Documents/pythonbootcamp/pythonBootcamppractice/dictionaries/dictionaryMethods.py
#None


#copy - makes a copy of the dictionary
instructors = instructor.copy()
print(instructors)

#fromkeys - creates key-value pairs deom comma seperated values:
{}.fromkeys("a","b") # {'a' : 'b'}
{}.fromkeys(["email"], 'unknown') # {'email': 'unknown'}
{}.fromkeys("a",[1,2,3,4,5]) # { 'a': [1,2,3,4,5]}

new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
print(new_user)
valuefornewuser = {}.fromkeys(['phone'], 'unknown')
new_user2 = dict.fromkeys(new_user, valuefornewuser)
print(new_user2)

#get - retrieves a key in an object and return None instead of a KeyError if the key does not exist
d = dict(a=1, b=2, c=3)
d['a'] #1
d.get('a') # same as above , 1
#d['no_key'] #KeyError
#d.get('no_key') # None  ### it will give you a None when their is no key

