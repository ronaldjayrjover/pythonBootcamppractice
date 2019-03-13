###1. return on wrong identation

def sum_odd_numers(num):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total
print(sum_odd_numers([1,2,3,4,5])) ### result will only be number 1 because the return on the IF conditions already returned the total

def sum_odd_numers(num):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total ## this is the right placement of the return so the IF condition will still loop



###2. unnecessary "else"

def is_odd_number(num):
    if val % 2 != 0:
        return True
    else:
        return False

#rewriting to correct format because if the statement is false it will jsut return False in the first place.

def is_odd_number(num):
    if val % 2 != 0:
        return True
    return False