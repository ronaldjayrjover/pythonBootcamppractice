'''
reversed
    return a reverse iterator
    its different with the .reverse() function
'''
nums = [1,2,3,4]
#nums.reverse()
reversed(nums)
print(list(reversed(nums)))

for char in list(reversed("hello")):
    print(char)

'''
len
    length - return the length (the number of items) of an object.
'''
print(len('adfadsfadfaf'))
print(len({"s": 2, "a": 3}))

'''
abs
    return the absolute value of a number. 
'''
abs(-23) #23
abs(3.44) #3.44

'''
sum
    takes an iterable and an optional and returns the sum of start and the items of an iterable from left to right and returns the total
'''
sum([1,2,3]) #6
sum([1,2,3], 10) #16
sum([1,2,3], -6) #0
sum(['hi', 'there']) # cant sum strings use ''.join(seq) instead

'''
round
    rounding off of integers
'''