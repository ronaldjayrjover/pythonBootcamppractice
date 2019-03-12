list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!

answer1 = {list2[i]: list1[i] for i in range(0,3)}
print(answer1)
answer2 = dict(zip(list1,list2))
print(answer2)