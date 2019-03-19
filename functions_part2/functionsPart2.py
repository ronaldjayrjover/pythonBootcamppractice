# single * operator or *args
#a special operator we can pass to functions, gathers remining arg as a tuple, this is just a parameter
#it can make your function be more flexible
def sum_all_nums(*args):
    total = 0
    for val in args:
        total += val
    return total

print(sum_all_nums(4,5,6,7))
print(sum_all_nums(2,3,4))

def ensure_correct_info(*args):
    print(args)
    if "jay" in args and "ron" in args:
        return "Hi jay"
    return "hu U"
print(ensure_correct_info("hello", 'jay', 'ron', 2))
print(ensure_correct_info("hello", 'jay', 2))

def sum_all_nums2(*nums): ### as long as the * is there
    total = 0
    for val in nums:
        total += val
    return total
print(sum_all_nums2(4,5,6,7))
print(sum_all_nums2(2,3,4))


#### ** kwargs - keyword args, a special operator we can pass to functions, gathers remaining keyword arguments
#as a dictionary, this is just a paramter -

def fav_colors(**kwargs):
    for person, color in kwargs.items(): ### because its already a dictionary thats why you need .items to loop inside the kwargs
        print(f"{person} fav color is {color}")

fav_colors(jay='red', jop='purple')


def special_greeting(**kwargs):
    if "ronron" in kwargs and kwargs["ronron"] == "special":
        return "hey hey hey"
    elif 'ronron' in kwargs:
        return f"{kwargs['ronron']} wazzzup!"
    return "hu u"

print(special_greeting(ronron="Hello"))
print(special_greeting(ronron="special"))
print(special_greeting(jayjay="Heloooooooo"))