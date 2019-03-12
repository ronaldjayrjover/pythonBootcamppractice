print({x**2 for x in range(10)})
print({x:x**2 for x in range(10)})
print({char.upper() for char in 'hello'})

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'})

'''
Recap for TUPLES and SET


- tuples are ordered collections of elemets, they are immutable
- tuples are faster than lists and useful for protecting data
- sets are unordered collections of unique values
- sets and tuples can be created with{} and () or the set() or tuple() function
- set comprehension is useful when converting other data types to a set

'''
