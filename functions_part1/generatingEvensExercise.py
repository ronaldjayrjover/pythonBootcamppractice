#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
#inside the function you can construct the list using either a loop OR list comprehension.


#my answer
def generate_evens():
    for num in range(0,50):
        if num % 2 == 0:
            return num
        else:
            return "odd"
print(generate_evens())


# trainor's answer

#Generating evens using a list comprehension:
#
# def generate_evens():
#     return [x for x in range(1,50) if x%2 == 0]
# print(generate_evens())


#Generating evens using a loop:

def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result
print(generate_evens())

