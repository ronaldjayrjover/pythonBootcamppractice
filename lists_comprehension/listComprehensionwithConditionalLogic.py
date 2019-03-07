### List Comprehension with conditional logic


### below is the usual condition without list comprehension
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print(numbers)


nummod = [num *2 if num % 2 == 0 else num/2 for num in numbers]
print(nummod)

string_list =[str(numsss) for numsss in numbers]
s = "-"
s = s.join(string_list)
print(s)

print("#############################")
print("########### break ###########")

with_vowels = " This is so much fun "
joining = ''.join(char for char in with_vowels if char not in 'aeiou')
print(joining)

print("#############################")
print("########### break ###########")

dude = '...'.join(["cool", "dude"])
print(dude)

print("#############################")
print("########### break ###########")

list1 = ["Elie", "Tim", "Matt"]
list2 = [1,2,3,4,5,6]

answer = [name[0] for name in list1]
print(answer)

answer2 = [num for num in list2 if num % 2 == 0]
print(answer2)

print("#############################")
print("########### break ###########")

'''Problem on list comprehensions'''

#Using list comprehensions:
#solution answer from the course

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

#Using good old manual loops:

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)

