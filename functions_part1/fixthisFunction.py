# Without adding any new lines of code, make count_dollar_signs work as intended
#putting a comment for the original problem
# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == '$':
#             count += 1
#         return count
#the word is $uper $ize  ##### it only gives 1 because once it saw the first $, it will end becuase the return in under IF condition

# Without adding any new lines of code, make count_dollar_signs work as intended
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

print(count_dollar_signs('$uper $ize'))