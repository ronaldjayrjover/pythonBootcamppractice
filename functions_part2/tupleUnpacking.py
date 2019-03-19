# using * as an argument : Argument Unpacking,  we can use * as an argument to a function to "unpack" values

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)
    print(nums)
nums = [1,2,3,4,5,6]
sum_all_values(*nums) ### by providing or entering * on the nums, we are passing it as an argument to the function