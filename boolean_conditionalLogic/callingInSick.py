'''
In this exercise you will be given a few variables that will be set randomly
to Boolean values (True or False)

actually_sick - when you legit have the flu
kinda_sick - you're feeling under the weather and its enough to treat yourself with a day off
hate_your_job - work sucks, i know....

You're also given a random number of sick_days between 0 and 10
Finally there is a variable called calling_in_sick that you must set to True or False based
on the following:

SetTrue if
    youre actually_sick and you have sick_days remaining
    you're kinda_sick and hate_your_job and you have sick_days remainin
Otherwise, set to False

The test check the value of calling_in_sick is correct based on the conditions specified above

'''



# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================

calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(actually_sick)
print(kinda_sick)
print(hate_your_job)
print(sick_days)

if actually_sick is True and sick_days >= 0:
    calling_in_sick = True
elif sick_days >= 0 and (kinda_sick is True and hate_your_job is True):
    calling_in_sick = True
else:
    calling_in_sick = False

print(calling_in_sick)

##### 1st try sa udemy gumagana heehheheh

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
