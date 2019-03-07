#collection or grouping of items!


# tasks = ["Install python", "Learn Python", "Take a break"]
#
# demo_list = ["a", 1,45, True, 6.7777]
# print(demo_list)
# print(len(demo_list))
#
# r = range(1,100)
# num = list(r)


friends = ["ashley", "matt", "michael"]

print("------------------------break-------------------------------")
# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
#Change "Hanna" to "Hannah"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = "Aparna"


print(people[0])
print(people[4])
print(people[-1])

print("------------------------break-------------------------------")


# colors = ["colors", "teal", "magenta", ]
#
# for color in colors:
#     print(color)

numbers = [4,5,3,6,1,9,13]
for num in numbers:
    print(num * num)
print("------------------------break-------------------------------")

colors = ["colors", "teal", "magenta", "crimson", "emerald"]
index = 0

while index < len(colors):
    print(colors[index])
    index += 1
print("------------------------break-------------------------------")

###Exercise
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
#write code that will lop through the list and add all the strings together to form
#one large combinded string
#the combined string should be in upper case
#save to variable "result"
result = ""
for i in sounds:
    result += i.upper()
print(result)

result = ''
for s in sounds:
    result += s
result = result.upper()
print(result)
print("------------------------break-------------------------------")