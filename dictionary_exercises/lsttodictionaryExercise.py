person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#create a dictionary called answer, that makes each first item in each list a key
#and the second itm a correposnding value, thats a terrible explanation. i think itll be easier if you just look at the end goal:

### end goal ===== {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

# use the person variable in your answer
answer = dict(person)
print(answer)

#####Other Solutions#####
###Using a dictionary comprehension

person2 = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer2 = {thing[0]: thing[1] for thing in person}
print(answer2)

#An alternate solution using a dict comprehension, without any references to list indexes:
person3 = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer3 = {k:v for k,v in person}
print(answer3)

#Finally, a really simple solution.  If you have a list of pairs, you can very easily turn it into a dictionary using dict()

#person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#answer = dict(person)