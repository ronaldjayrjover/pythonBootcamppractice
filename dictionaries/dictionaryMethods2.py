#pop - take a single argument correposnding to a key and removes that key-value pair from the dictionary.
#returns the value corresponding to the key that was removed

instructor = {
    "name": "jay",
    "age": 36,
    "state": "quezon",
    "color": "blue"
}

#print(instructor.pop("name"))
#print(instructor.popitem())
#print(instructor)

#popitem = random


#update update the keys and values in a dictionary with another set of key value pairs

person = {"city": "manila"}
print(person)
print(person.update(instructor))

#####GUMANA SA INTERPRESTER#####
'''Python 3.6.5 (default, Apr 25 2018, 14:23:58)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
    >>> instructor = {"name": "jay", "state": "quezon"}
>>> intructor
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'intructor' is not defined
>>> instructor
{'name': 'jay', 'state': 'quezon'}
>>> person = {"city": "manila"}
>>> person.update(instructor)
>>> person
{'city': 'manila', 'name': 'jay', 'state': 'quezon'}
>>>
'''
