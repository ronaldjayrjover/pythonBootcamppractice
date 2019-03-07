#the syntax:
#[ _ for _ in __]
nums = [1, 2, 3]
num = [x*10 for x in nums]
print(num)
print("########## break ############")

'''List comprehension vs Looping'''

# Looping
numbers = [1, 2, 3, 4, 5]
doubleNumbers = []

for num in numbers:
    doubleNumber = num * 2
    doubleNumbers.append(doubleNumber)
print("Start of Loop")
print(doubleNumbers)

# List Comprehension
numbersLC = [1, 2, 3, 4, 5]
doubleNumbersLC = [num * 2 for num in numbersLC]
print("Start of List Comprehension")
print(doubleNumbersLC)


print("########## break ############")

name = 'colt'
namenew = [char.upper() for char in name]
print(namenew)

friends = ['ashley', 'matt', 'matthew']
friendsnew = [friend[0].upper() for friend in friends]
print(friendsnew)

print("########## break ############")

numsnew = [numss*10 for numss in range(1,6)]
print(numsnew)

boolval = [bool(val) for val in [0, [], '']]
print(boolval)

numberss = [1, 2, 3, 4, 5]
string_list =[str(numsss) for numsss in numberss]
print(string_list)