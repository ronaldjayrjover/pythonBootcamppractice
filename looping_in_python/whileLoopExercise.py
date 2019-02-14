'''
from random import randint  # use randint(0, 10)
to generate a random number between a and b
'''
from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

#####my first try nag loop siya#####
# number = randint(0, 10)
# print(number)
#
# while number != 5:
#     print(number)
#     i += 1
#     print(i)



while number != 5:
    i += 1
    number = randint(0, 10)
    print(f" how many iteration {i} , {number}")