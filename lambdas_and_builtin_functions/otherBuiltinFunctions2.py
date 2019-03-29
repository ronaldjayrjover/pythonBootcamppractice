'''
all
    return true if all elements of the iterable are true else false
'''

print([char for char in 'eio' if char in 'aeiou'])
print(all([char for char in 'eio' if char in 'aeiou']))

print([num for num in [2,4,6,8] if num % 2 == 0])
print(all([num for num in [2,4,6,8] if num % 2 == 0]))

people = ["Che", "Cris", "Cas"]
print(all(name[0] == "C" for name in people))

peoplea = ["Che", "Cris", "Cas", "kay"]
print(all(name[0] == "C" for name in peoplea))

'''
any
    return true if any elements of the iterable are true else false
'''

nums = [0,1,2,3]
print(any(numss % 2 == 0 for numss in nums))


'''
generator expression
    remove the list bracket, it differs in terms that list comprehension you need to save and do something
    but generator expression is you just need to pass meaning once done its done no more commands


    below is just an example on how much memory list comprehension versus generator
    
    you can use both, up to you.
'''

import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
generator_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"list comprehension: {list_comp} bytes")
print(f"generator expression: {generator_exp} bytes")
