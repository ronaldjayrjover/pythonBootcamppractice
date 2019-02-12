'''SOLUTION
Section 10, Lecture 85
Solution Using a Conditional

This solution loops over all the numbers between 10 and 20, checking to see if the number is even inside the loop.

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0


# YOUR CODE GOES HERE:
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n


Solution using range step
Instead of looping over every number between 10 and 20, this solution only loops over the odd numbers.  Remember, the 3rd argument to range() is the STEP or interval that you want the range to increment by. Thanks for sharing your version, Abdul.

x = 0

for i in range(11,21,2):
        x += i
'''
# Use a for loop to add up every odd number odd number 10 to 20 (inclusive)
# and store the result in the variable x.

x = 0


# YOUR CODE GOES HERE:
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n
    print(x)


#Solution using range step
#Instead of looping over every number between 10 and 20, this solution only loops over the odd numbers.  Remember, the 3rd argument to range() is the STEP or interval that you want the range to increment by. Thanks for sharing your version, Abdul.

x = 0

for i in range(11,21,2):
    x += i
    print(x)